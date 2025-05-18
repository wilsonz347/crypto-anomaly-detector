# Crypto Anomaly Detection

This project performs anomaly detection on Bitcoin prices using machine learning, with model serving and CI/CD automation powered by BentoML and GitHub Actions.

---

## Project Overview

- **Exploratory Data Analysis (EDA):**  
  Analyze and visualize Bitcoin price data to understand patterns and detect anomalies.

- **Tools Used:**  
  - Python  
  - Pandas, NumPy  
  - Scikit-learn (Isolation Forest)  
  - BentoML (model serving)  
  - GitHub Actions (CI/CD pipeline)

- **Isolation Forest Training:**  
  Train an Isolation Forest model to detect anomalies in Bitcoin price data.

- **Model Saving with BentoML:**  
  Save the trained model and scaler to the BentoML model store for efficient versioning and deployment.

- **API Development with BentoML Service:**  
  Load the saved model and scaler, then build an API endpoint to serve anomaly predictions.

- **Configuration:**  
  Use `bentofile.yaml` to configure your BentoML service.

- **CI/CD Pipeline:**  
  Automated build and deploy pipeline using GitHub Actions, triggered on pushes to the `main` branch.

---

## Dataset

The cryptocurrency price history dataset used in this project is available on Kaggle:

[Cryptocurrency Price History by Sudalai Rajkumar](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory)

---

## How to Use

1. Clone the repository  
2. Explore the EDA notebook or script to understand the data  
3. Train the Isolation Forest model and save it to BentoML store  
4. Use the BentoML service to expose prediction API  
5. Configure deployment in `bentofile.yaml`  
6. Push changes to `main` branch to trigger CI/CD pipeline  

---

## CI/CD Pipeline

- Installs dependencies  
- Builds BentoML service  
- (Optional) Runs tests  
- (Optional) Deploys to a cloud service  

Check the **Actions** tab in this repository for pipeline run status and logs.

---

## License

MIT License

---

## Use of AI Assistance

This project leveraged advanced AI language models, including OpenAI's ChatGPT and Anthropic's Claude, to streamline several key aspects of development, such as:

- **Debugging:** Rapid identification and resolution of coding issues.
- **Reporting:** Generation of detailed analysis reports and summaries.
- **Documentation:** Creation and refinement of technical documentation and comments.

The integration of AI tools helped accelerate the development process, improve code quality, and ensure thorough, clear communication throughout the project lifecycle.