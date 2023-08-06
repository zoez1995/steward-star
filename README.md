## 💫 StewardStar - Your Data Quality Commandar Powered by GenAI 🧙

Have you ever looked at some data but don't know what you are looking at? Have you spent hours validating your data manually and more hours creating the data validation report?
StewardStar got you coverd! Simply upload the data you want to validate, and StewardStar will generate the validation report you need.
You can customize your validation by giving StewardStar a context, or you can simply leverage StewardStar for general purpose data validation.
![image](https://github.com/zoez1995/steward-star/assets/16796687/aee03054-830b-43f3-af5c-3d8074730819)

### Let's start with a simple example to see how StewardStar works without context

**Go to "Diagose Data" page, and upload your data, you will see a data preview once you upload your data file**
![image](https://github.com/zoez1995/steward-star/assets/16796687/cac7c43e-ae21-4220-be37-c7f67fd58714)

**Ask some questions about your data, then click "Generate Report"**
![image](https://github.com/zoez1995/steward-star/assets/16796687/b1392bdf-8061-438c-aeec-38871f920cca)

**Get your validation report**
![image](https://github.com/zoez1995/steward-star/assets/16796687/44fd8e0c-dd7d-48b6-a086-65b689436d65)


### Here's an example of StewardStar working with context

**In "Diagnose Data" page, upload your context, in this example, we use the DDL for the data we want to validate as the context**
![image](https://github.com/zoez1995/steward-star/assets/16796687/cbd53124-8b95-411d-a094-e7c8df903eaf)

**Then upload the data and ask questions**
![image](https://github.com/zoez1995/steward-star/assets/16796687/d6e05157-4ef8-4200-9e34-66ab48fba31f)

**Generate the validation report, and you can see StewardStar validates the data against its DDL, and pointed out there's an extra column in the data**
![image](https://github.com/zoez1995/steward-star/assets/16796687/9ee534bd-2175-41d3-b0d5-ac11ed8fb898)


### You can also ask questions about multiple data sets at once
![image](https://github.com/zoez1995/steward-star/assets/16796687/f4712c67-4dee-4658-b60c-3aff28cbac59)

![image](https://github.com/zoez1995/steward-star/assets/16796687/8aee7927-09ff-498f-84bd-ddd7702e3e8f)

![image](https://github.com/zoez1995/steward-star/assets/16796687/1f993b59-5c77-4cfb-8f8d-1e8da3c7fe70)

![image](https://github.com/zoez1995/steward-star/assets/16796687/3111fffa-6853-4020-9ec8-00c8bb8b90f0)


### Monitor your Data Quality KPIs

**Let's look at this customer data example**
![image](https://github.com/zoez1995/steward-star/assets/16796687/09e4c8a4-b4d3-47a3-8448-d600372927b7)
![image](https://github.com/zoez1995/steward-star/assets/16796687/11e6df00-9f83-4e2c-94ff-4d300801509f)

**Yeah, it's cool that you can directly get a data quality report from StewardStar, but as a visual person, you want to visualize the findings. This is when you head to the "Visualize Data" page. The page will auto detect the data you uploaded on the "Diagnose Data" page, and auto-generate a chart for your data. In this example, we have a bar chart of the percentage of null value in your data.**
![image](https://github.com/zoez1995/steward-star/assets/16796687/d8a262e7-4f03-4051-931e-c8b1880a7549)


**Now you may ask, what's the "so what" of this chart? What action should I take from seeing these numbers? Here's what you can do: click the "Check data quality KPI Health" button below the chart, and StewardStar will help you interpret how these null values impact the overall performance of data quality KPI**
![image](https://github.com/zoez1995/steward-star/assets/16796687/107964f2-6a00-4baf-a290-83233fefb156)


### Communicate your findings

**After diagnosing and visualizing the data, you have an understanding of issues in the data and an action plan. Now you need to communicate your findings and recommendations to the data owner. Now let's navigate to the "Generate Communication" page, and have StewardStar help you generate the email communication draft. You can specify the person or team you are sending the email to, and pick the urgency level of the communication. StewardStar will customize the email based on the information you provided.**
![image](https://github.com/zoez1995/steward-star/assets/16796687/d2a00b54-3296-4908-b89a-872489e3cafa)

**Click the "Generate Communication Message" button, and there you go - an email draft that's ready for your review**
![image](https://github.com/zoez1995/steward-star/assets/16796687/02b37da2-dad1-43b9-a6c0-1064bed3fcd5)

**I hope you become a happy data steward with the help from StewardStar 💫**

## How to run the solution

In your terminal, run `streamlit run .\home_page.py` to launch StewardStar. Make sure to modify the .env file with the corresponding Azure OpenAI API configuration before running the code.


