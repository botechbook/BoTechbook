# Example of Calculating the Mahalanobis Distance | James D. McCaffrey

If you work with machine learning (making predictions from data), you’ll eventually run into the Mahalanobis Distance (MD). The MD is a measure of distance between a data vector and a set of data, or a variation that measures the distance between two vectors from the same dataset Suppose you have data for five people, and each person vector has a Height, Score on some test, and an Age:

```
X       Y       Z
Height  Score   Age
64.0    580.0   29.0
66.0    570.0   33.0
68.0    590.0   37.0
69.0    660.0   46.0
73.0    600.0   55.0

m =68.0 600.0   40.0

n=5

```

The mean of the data is (68.0, 600.0, 40.0). Now suppose you want to know how far another person, v = (66, 640, 44), is from this data. It turns out the Mahalanobis Distance is 5.33 (no units).

Intuitively, you could just look at how far v (66, 640, 44) is from the mean of the dataset (68.0, 600.0, 40.0). But the Mahalanobis Distance also takes into account how far the Height, Score, and Age values are from each other.

The MD uses the covariance matrix of the dataset – that’s a somewhat complicated side-topic (see my previous blog post on that topic).

Mathematically, the MD is defined as:

![Example%20of%20Calculating%20the%20Mahalanobis%20Distance%20Ja%20cfefce9273b9449e89090d580ff9043d/mahalanobisequation.jpg](Example%20of%20Calculating%20the%20Mahalanobis%20Distance%20Ja%20cfefce9273b9449e89090d580ff9043d/mahalanobisequation.jpg)

The top equation is the usual definition. The bottom equation is a variation of MD between two vectors instead of one vector and a dataset.

In the Excel spreadsheet shown below, I show an example. First you calculate the covariance matrix, (S in the equation, “covar mat” in the image). Then you find the inverse of S (“inv-covar” in the image).

![Example%20of%20Calculating%20the%20Mahalanobis%20Distance%20Ja%20cfefce9273b9449e89090d580ff9043d/mahalanobisinexcelexamplecalcs.jpg](Example%20of%20Calculating%20the%20Mahalanobis%20Distance%20Ja%20cfefce9273b9449e89090d580ff9043d/mahalanobisinexcelexamplecalcs.jpg)

Then you subtract the mean from v: (66, 640, 44) – (68.0, 600.0, 40.0) to get v-m = (-2, 40, 4). Then you matrix-multiply that 1×3 vector by the 3×3 inverse covariance matrix to get an intermediate 1×3 result tmp = (-9.9964, -0.1325, 3.4413). Then you multiply the 1×3 intermediate result by the 3×1 transpose (-2, 40, 4) to get the squared 1×1 Mahalanobis Distance result = 28.4573. The last step is to take the square root, giving the final Mahalanobis Distance = 5.33.

Mahalanobis Distance appears a bit complicated at first, but if you examine this example carefully, you’ll soon see it’s actually quite simple.

![Example%20of%20Calculating%20the%20Mahalanobis%20Distance%20Ja%20cfefce9273b9449e89090d580ff9043d/a_distance_settlement_eghosa_raymond_akenbor.jpg](Example%20of%20Calculating%20the%20Mahalanobis%20Distance%20Ja%20cfefce9273b9449e89090d580ff9043d/a_distance_settlement_eghosa_raymond_akenbor.jpg)

*“A Distance Settlement” – Eghosa Raymond Akenbor*