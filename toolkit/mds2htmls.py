#!/usr/bin/python3

import shutil
import os
import sys
import re
import logging
import logging.handlers
import argparse
from argparse import RawTextHelpFormatter
import markdown
# import pypandoc


Logger = logging.getLogger()

class Argument():

    def __init__(self, sysArgList):
        self.sysArgList = list(sysArgList)
        programName = self.sysArgList[0]
        cli_prompt = ''' [src folder path] [output folder path]

This program is to convert all the markdown files under src folder to html files saving into output foler.

Notes:
1. You must specify both src folder path and output folder path.
2. The program will replace all the links in markdown from [xx](yy.md) to [xx](yy.html).


        '''
        del self.sysArgList[0]
        self.arg_usage = '\n\n' + programName + cli_prompt
        self.parser = argparse.ArgumentParser(usage=self.arg_usage, formatter_class=RawTextHelpFormatter)

    def check_arg_limit(self):
        if len(self.remaining) < 2:
            self.print_help()
        else:
            if not os.path.isdir(self.remaining[0]) or not os.path.isdir(self.remaining[1]):
                self.print_help()


    def parse_args(self):
        # self.parser.add_argument('-p', '--private-key', dest='private_key', required=True, default=None,
        #                          help='Required, specify the private key to decrypt the password.')
        self.parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='Enable debug mode.')
        # self.parser.add_argument('-t', '--trello-enabled', dest='trello_enabled', action='store_true',
        #                          help='Enable the trello card making, it is not enabled by default.')

        self.args, self.remaining = self.parser.parse_known_args(self.sysArgList)

        self.debug = self.args.debug

        self.check_arg_limit()

    def print_help(self):
        self.parser.print_help()
        exit()


def setSimpleLogging(debug=True):
    logger = logging.getLogger()
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    handlersList = list(logger.handlers)
    if handlersList != []:
        for i in handlersList:
            logger.handlers.remove(i)

    consoleHandler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    myFilter = logging.Filter(name='root')
    logger.addFilter(myFilter)

    # filter = logging.Filter('mylogger.child1.child2')
    # fileHandler.addFilter(filter)
    # logger.addFilter(filter)



def convert_markdowns_to_htmls(src_dir, output_dir):
    Logger.debug("Converting markdown files under " + str(src_dir) + " to " + str(output_dir) + " ...")
    listdir_result = os.listdir(src_dir)
    for i in listdir_result:
        current_path = os.path.join(src_dir, i)
        if os.path.isfile(current_path):
            if str(current_path).endswith(".md"):
                Logger.info("Converting: " + str(current_path) + " to " + os.path.join(output_dir, str(i)[0:-3] + ".html"))
                with open(current_path, "r", encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    md_links = re.findall(r"\[.*\]\(.*\.md\)", md_content)
                    for md_link in md_links:
                        md_content = md_content.replace(md_link, md_link[0:-3]+"html)")
                    # pypandoc.convert_file(current_path, "html", outputfile=os.path.join(output_dir, str(i)[0:-3] + ".html"))
                    # pypandoc.convert_text(md_content, "html", format="md", outputfile=os.path.join(output_dir, str(i)[0:-3] + ".html"))
                    html_content = markdown.markdown(md_content, output_format="html")
                    with open(os.path.join(output_dir, str(i)[0:-3] + ".html"), "w", encoding='utf-8') as html_file:
                        html_file.write(html_content)
                
            else:
                Logger.info("Copying: " + current_path + " to " + os.path.join(output_dir, i))
                shutil.copyfile(current_path, os.path.join(output_dir, i))
                
        elif os.path.isdir(current_path):
            Logger.info("Creating dir: " + str(os.path.join(output_dir, i)))
            os.makedirs(os.path.join(output_dir, i), exist_ok=True)
            convert_markdowns_to_htmls(current_path, os.path.join(output_dir, i))


def main(args):
    my_args = Argument(args)
    my_args.parse_args()

    is_debug = my_args.debug
    src_folder = my_args.remaining[0]
    output_folder = my_args.remaining[1]
    setSimpleLogging(debug=is_debug)

    convert_markdowns_to_htmls(src_folder, output_folder)


if __name__ == "__main__":
    main(sys.argv)






