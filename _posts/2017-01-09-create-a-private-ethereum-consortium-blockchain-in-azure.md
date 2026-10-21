---
layout: post
title: "Create a private #Ethereum #Consortium #Blockchain in #Azure"
date: 2017-01-09
description: "Private Blockchain network template in Azure"
image: https://cdn-images-1.medium.com/max/2560/1*S_3lUOHDQoSjpoRemZsJHw.jpeg
tags: ["Blockchain", "Azure"]
---

### Create a private #Ethereum #Consortium #Blockchain in #Azure

![](https://cdn-images-1.medium.com/max/2560/1*S_3lUOHDQoSjpoRemZsJHw.jpeg)

### **Private Blockchain network template in Azure**

In this tutorial, I demonstrate how to create a private [Ethereum](https://www.ethereum.org/) Consortium Blockchain network in Azure using one of the Azure Marketplace templates.

To begin the process, login to Azure portal and click on the “+” icon on top left corner.

Then in the search box, type in ”blockchain” and it will show you all the available templates with this name, and select the one called: “Ethereum Consortium Blockchain” by published Microsoft.

![](https://cdn-images-1.medium.com/max/1200/1*dHsPLrHOP9lnsGKEYg6l9g.png)*Ethereum Blockchain template from Azure Market place*

Now, on the right side (following picture), you will see a description of the template and a nice picture of the components it is going to deploy for us.

![](https://cdn-images-1.medium.com/max/1200/1*85mJeTlt-ZyuROzxwwkTKw.png)*Ethereum Blockchain Template in Azure Marketplace description*

The following picture shows, what this template is going to deploy and how these component are connected to each other. Note that this is the current template definition and obviously it might change in the future by Microsoft.

![](https://cdn-images-1.medium.com/max/800/1*_AbJBsgQhMKCAO0T-HI_ww.png)*The Ethereum template will create this network in Azure*

### Configure basic settings

First tab is “Basic” which you provide the Resource Group name, Location and the name and password for the VMs that are being provisioned.

![](https://cdn-images-1.medium.com/max/800/1*xc5PlsMCpL-C3Gmp7xCi7g.png)*Resource Groups and VM user name password for the Ethereum network*

### Network size and performance

The second tab, is about selecting the size and the plan of the VMs that are being created. For more details around the [prices](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/) and configuration of each VM instance you can check the [Azure portal](https://docs.microsoft.com/en-us/azure/virtual-machines/virtual-machines-windows-sizes).

![](https://cdn-images-1.medium.com/max/800/1*pQbhOv6WVqj0UWKT0aFePA.png)*VM Size and Service plan selection for the Ethereum Network*

### Ethereum Settings

The third tab, is about the Ehereum network settings.

**Network ID**

Each Ethereum network has its own Network ID, with 1 being the ID for the public network. While we have restricted network access for mining nodes, we still recommend using a large number to prevent collisions.

Any value between 5 and 2,147,483,647 is allowed for Network ID.

**Ethereum Account Password**

The administrator password used to secure the Ethereum account imported into each node. This account is setup in the [genesis block](https://en.bitcoin.it/wiki/Genesis_block) and pre-allocated with one *trillion Ether*.

**Ethereum private key passphrase**

The passphrase used to generate the [ECC private key](https://en.wikipedia.org/wiki/Elliptic_curve_cryptography) associated with the default Ethereum account that is generated. A pre-generated private key does not need to be explicitly passed in.

![](https://cdn-images-1.medium.com/max/800/1*mh1BKIfND7DH4ysgMpqiog.png)*Ethereum settings page in Azure Portal*

### Summary Tab

Click through the summary blade to review the inputs specified and to run basic pre-deployment validation.

![](https://cdn-images-1.medium.com/max/800/1*KMMiMnH_t7OROBbxrAyx4A.png)*Summary page of the Ethereum network*

### **Buy Tab**

The last tab is the legal and licenses stuff. Take a minute to review them and click on the Purchase button to start the deployment.

![](https://cdn-images-1.medium.com/max/800/1*UJwEfZsjyaUZY2P-gLcgLA.png)*Terms and Conditions for deploying the Ethereum network*

Once you clicked on Purchase, Azure will start the deployment of all the pieces for you. When I tried this for the basic settings (all default values and default VM sizes) took about 15 minutes to finish the deployment.

![](https://cdn-images-1.medium.com/max/800/1*HI4_AJMYylc76SdXNwEYEQ.png)*Azure in the middle of deploying Ethereum network components*

After the deployment is done, you can go to the “All resources” tab and see the components installed in the “ResourceGroup” you selected. In my case the resource group name was “EthereumAram” as you can see in the following picture.

![](https://cdn-images-1.medium.com/max/800/1*f0DtyQfhLyd9zbYodzZtfQ.png)*All Ethereum components deployed to Azure*

### Opening the deployed Admin Portal

To open the Admin portal for this network that was deployed, click the Resource Group, and click on he Deployments link (Says “5 Succeeded” in the following picture)

![](https://cdn-images-1.medium.com/max/800/1*k85QXvi0lpHZkvh8c5ReyQ.png)*Azure Resouce group that all the Ethereum components are created there*

Then click on the first item in the list. Says “microsoft-azure-mlockchain.azure-block…” in the following picture. Now in the right hand you can see the “ADMIN-SITE” url.

![](https://cdn-images-1.medium.com/max/800/1*gDXrTWDx0r8Kq4PuEQfbGg.png)*The Load Balancer DNS settings that displays the Admin Site and the Ethereum RPC Endpoint*

Then you open that Admin Portal you can see the different Nodes hosted and some information about “Latest Block Number”, “Peer Count” etc.

In the following picture the nodes ending in mn0 and mn1 are miner nodes and the node ending in tx0 is the transaction node

![](https://cdn-images-1.medium.com/max/1200/1*-yYoMloS2uabUxqsbWn9Eg.png)*Private Ethereum network Admin Page*

Obviously , this is just a starting point, and you can make changes to this network, create your own template and save it for your own future use if needed. And then you can implement your cool idea on top of blockchain in your private ethereum network hosted in Azure.

### Book Recommendation

Here are some book recommendation if you are interested:

[**Ethereum: Blockchains, Digital Assets, Smart Contracts, Decentralized Autonomous Organizations**  
*Blockchain For the Non-Technical \*\*\* THIS IS A PREVIEW PRINT \*\*\* As IBM´s official liaison to the Ethereum core…*www.amazon.com](https://www.amazon.com/gp/product/1523930470/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1523930470&linkId=c82362da36588ebb20b557d2fbf25df3 "https://www.amazon.com/gp/product/1523930470/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1523930470&linkId=c82362da36588ebb20b557d2fbf25df3")

<https://www.amazon.com/gp/product/1491971940/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491971940&linkId=3c156e0927d49236b14f139d0450c554>

[**Introducing Ethereum and Solidity: Foundations of Cryptocurrency and Blockchain Programming for…**  
*Learn how to use Solidity and the Ethereum project — second only to Bitcoin in market capitalization. Blockchain…*www.amazon.com](https://www.amazon.com/gp/product/1484225341/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484225341&linkId=290599f896e774b8890420998653660f "https://www.amazon.com/gp/product/1484225341/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484225341&linkId=290599f896e774b8890420998653660f")
