# Bray-Curtis Dissimilarity: Definition & Examples - Statology

Named after [J. Roger Bray](https://en.wikipedia.org/wiki/J._Roger_Bray) and [John Thomas Curtis](https://en.wikipedia.org/wiki/John_Thomas_Curtis), the **Bray-Curtis Dissimilarity** is a way to measure the dissimilarity between two different sites.

It’s often used in ecology and biology to quantify how different two sites are in terms of the species found in those sites.

The Bray-Curtis Dissimilarity is calculated as:

**BCij = 1 – (2*Cij) / (Si + Sj)**

where:

- **Cij:** The sum of the lesser values for the species found in each site.
- **Si:** The total number of specimens counted at site *i*
- **Sj:** The total number of specimens counted at site *j*

The Bray-Curtis Dissimilarity always ranges between 0 and 1 where:

- **0** indicates that two sites have zero dissimilarity. In other words, they share the exact same number of each type of species.
- **1** indicates that two sites have complete dissimilarity. In other words, they share none of the same type of species.

The following example shows how to calculate the Bray-Curtis Dissimilarity for two sites.

### **Example: Calculating the Bray-Curtis Dissimilarity**

Suppose a botanist goes out and counts the number of five different plant species (A, B, C, D, and E) in two different sites.

The following table summarizes the data she collected:

![Bray-Curtis%20Dissimilarity%20Definition%20&%20Examples%20-%20%20846a0895f08142c985bf40bb46b8e052/bray_curtis.png](Bray-Curtis%20Dissimilarity%20Definition%20&%20Examples%20-%20%20846a0895f08142c985bf40bb46b8e052/bray_curtis.png)

Using this data, she can calculate the Bray-Curtis dissimilarity as:

![Bray-Curtis%20Dissimilarity%20Definition%20&%20Examples%20-%20%20846a0895f08142c985bf40bb46b8e052/bray_curtis2.png](Bray-Curtis%20Dissimilarity%20Definition%20&%20Examples%20-%20%20846a0895f08142c985bf40bb46b8e052/bray_curtis2.png)

Plugging these numbers into the Bray-Curtis dissimilarity formula, we get:

- BC = 1 – (2*C) / (S + S)
    
    ij
    
    ij
    
    i
    
    j
    
- BC = 1 – (2*15) / (21 + 24)
    
    ij
    
- BC = 0.33
    
    ij
    

The Bray-Curtis dissimilarity between these two sites is **0.33**.

### **Key Assumption of the Bray-Curtis Dissimilarity**

The Bray-Curtis dissimilarity assumes that the two sites are of equal size.

This is a crucial assumption because if one site is four times larger than the other site, then we’ll naturally count more species in the larger site compared to the smaller site simply because there is so much more area to cover.

To illustrate this, suppose that one of the sites that the botanist collected data for was four times larger than the other site:

![Bray-Curtis%20Dissimilarity%20Definition%20&%20Examples%20-%20%20846a0895f08142c985bf40bb46b8e052/bray_curtis3.png](Bray-Curtis%20Dissimilarity%20Definition%20&%20Examples%20-%20%20846a0895f08142c985bf40bb46b8e052/bray_curtis3.png)

We would expect much higher frequencies of the species in Site 1 simply because it’s so much larger than Site 2.

Thus, when we go to calculate the Bray-Curtis Dissimilarity, it would be quite large. However, this would be misleading because the difference between the two sites isn’t in their composition, but rather in their size.