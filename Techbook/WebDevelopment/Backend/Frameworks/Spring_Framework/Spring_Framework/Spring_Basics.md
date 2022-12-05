---

mindmap-plugin: basic

---

# Spring Basics

## Tutorials
[DigitalOcean Spring Tutorial](https://www.digitalocean.com/community/tutorials/spring-tutorial-spring-core-tutorial#spring-tutorial)
[Baeldung Spring Tutorial](https://www.baeldung.com/spring-tutorial)
[廖雪峰 Spring Tutorial](https://www.liaoxuefeng.com/wiki/1252599548343744/1266263217140032)

## Spring Core Concepts

- Container
	
	Provide support for components running environment.
	
	- Tomcat is a Servlet container
	- `JavaBeans`
		- encapsulate one or more objects into a single standardized object (the bean)
		- Object in Spring IoC container is called `JavaBean`
		- In XML configuration file, a `JavaBean` is a `Bean`
	- Spring IoC container
		- An IoC container is a common characteristic of frameworks that implement IoC.
		- The Spring container is responsible for:
			- Instantiating objects (beans)
			- Configuring objects (beans)
			- Assembling objects (beans)
			- Managing life cycles of objects (beans)
		- IoC container interface:
			- `ApplicationContext` represents the IoC container
				- standalone applications implementation (`Class`):
					- `ClassPathXmlApplicationContext`
					- `FileSystemXmlApplicationContext`
				- web applications implementation (`Class`):
					- `WebApplicationContext`
				- `ApplicationContext` example
				
					```Java
					// context is an IoC container
					ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");

					// 从`ApplicationContext`中我们可以根据Bean的ID获取Bean，但更多的时候我们根据Bean的类型获取Bean的引用
					UserService userService = context.getBean(UserService.class);


					User user = userService.login("bob", "password");
					System.out.println(user.getName());
					```
			- `BeanFactory` Container
			
				`BeanFactory`和`ApplicationContext`的区别在于，`BeanFactory`的实现是按需创建，即第一次获取Bean时才创建这个Bean，而`ApplicationContext`会一次性创建所有的Bean。实际上，`ApplicationContext`接口是从`BeanFactory`接口继承而来的，并且，`ApplicationContext`提供了一些额外的功能，包括国际化支持、事件和通知机制等。通常情况下，我们总是使用`ApplicationContext`，很少会考虑使用`BeanFactory`

				```Java
				BeanFactory factory = new XmlBeanFactory(new ClassPathResource("application.xml"));
				MailService mailService = factory.getBean(MailService.class);
				```


- IoC (Inversion of Control)

	We can achieve Inversion of Control through various mechanisms such as: Strategy design pattern, Service Locator pattern, Factory pattern, and `Dependency Injection (DI)`
	> [==**IoC原理**==](Spring_Basics/IoC原理.md)

	- Advantages
		-   decoupling the execution of a task from its implementation
		-   making it easier to switch between different implementations
		-   greater modularity of a program
		-   greater ease in testing a program by isolating a component or mocking its dependencies, and allowing components to communicate through contracts

- DI (Dependency Injection)	
	> [==**IoC DI with Spring**==](Spring_Basics/IoC_DI_with_Spring.md)
	
	- Create the config of beans through:
		- @Bean annotation
		- XML configuration
		
			```XML
			<beans>
			    <bean id="dataSource" class="HikariDataSource" />
			    <bean id="bookService" class="BookService">
			        <property name="dataSource" ref="dataSource" />
			    </bean>
			    <bean id="userService" class="UserService">
			        <property name="dataSource" ref="dataSource" />
			    </bean>
			</beans>
			```
			上述XML配置文件指示IoC容器创建3个JavaBean组件，并把id为`dataSource`的组件通过属性`dataSource`（即调用`setDataSource()`方法）注入到另外两个组件中。
	- ==Dependency Injection== in Spring can be done through:
			- `Constructor-Based` Dependency Injection
			- `Setter-Based` Dependency Injection
			- `Field-Based` Dependency Injection
			- `Autowiring` Dependencies
- AOP (Aspect oriented programming)



## Spring Architecture



