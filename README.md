# ChatDev Web Application User Manual

## Introduction

Welcome to the ChatDev Web Application User Manual! This manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use the application effectively.

The ChatDev Web Application is a comprehensive web interface that facilitates student participation in a bidding system. It allows students to input unique power plant names along with corresponding bid power and bid price. The application also provides a centralized main view for teachers to review all submitted bids. The system allows the teacher to set a demand level after all bids have been submitted, computes the market clearing price using a merit order algorithm, and dynamically plots the merit order within the browser window. The application securely stores all bid data for privacy and future analysis, offers real-time updates for bid submissions, demand setting, and price calculation, ensures scalability to accommodate multiple users concurrently, and guarantees a seamless and educational experience for all participants.

## Installation

To install and run the ChatDev Web Application, please follow the steps below:

1. Ensure that you have Python installed on your machine. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the ChatDev Web Application repository from GitHub: [https://github.com/chatdev/web-application](https://github.com/chatdev/web-application)

3. Open a terminal or command prompt and navigate to the cloned repository directory.

4. Create a virtual environment by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Start the web application by running the following command:

   ```
   python main.py
   ```

8. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the ChatDev Web Application.

## Main Functions

The ChatDev Web Application provides the following main functions:

1. **Submit Bid**: Students can input unique power plant names, bid power, and bid price using the "Submit Bid" form on the home page. Click the "Submit Bid" button to submit the bid.

2. **Set Demand Level**: Teachers can set the demand level after all bids have been submitted using the "Set Demand Level" form on the home page. Enter the demand level and click the "Set Demand Level" button to set the demand.

3. **Compute Market Clearing Price**: Teachers can compute the market clearing price using the "Compute Market Clearing Price" button on the home page. The market clearing price will be displayed if it can be computed based on the submitted bids and the set demand level.

4. **Clear Bids**: Teachers can clear all submitted bids and reset the demand level using the "Clear Bids" button on the home page.

## Usage Instructions

To use the ChatDev Web Application effectively, follow the instructions below:

1. Open the ChatDev Web Application in a web browser by navigating to [http://localhost:5000](http://localhost:5000).

2. On the home page, students can submit their bids by entering the power plant name, bid power, and bid price in the "Submit Bid" form. Click the "Submit Bid" button to submit the bid.

3. Teachers can review all submitted bids in the "All Bids" table on the home page.

4. After all bids have been submitted, teachers can set the demand level by entering the desired demand level in the "Set Demand Level" form. Click the "Set Demand Level" button to set the demand.

5. Teachers can compute the market clearing price by clicking the "Compute Market Clearing Price" button. The market clearing price will be displayed if it can be computed based on the submitted bids and the set demand level.

6. Teachers can clear all submitted bids and reset the demand level by clicking the "Clear Bids" button.

## Conclusion

Congratulations! You have successfully installed and learned how to use the ChatDev Web Application. Enjoy facilitating student participation in the bidding system and providing a seamless and educational experience for all participants. If you have any further questions or need assistance, please refer to the documentation or contact our support team.
