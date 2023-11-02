# COVID-19 Statistics Notification Script

This is a Python script that fetches the latest COVID-19 statistics from a designated source and sends desktop notifications using the `plyer` library. The script allows you to stay updated on COVID-19 data for different states or regions.

## Getting Started

To run this script, you need to have Python installed on your system and install the required libraries. You can install `plyer` and `requests` using pip:

```shell
pip install plyer requests

git clone https://github.com/yourusername/covid-statistics-notifier.git
cd covid-statistics-notifier

python covid_stats_notifier.py
```
## Features
- **Customizable Source:** You can easily update the source URL to fetch data from different COVID-19 data providers.
- **Notification Alerts:** The script uses desktop notifications to keep you informed of COVID-19 statistics.
- **Error Handling:** Improved error handling to handle issues gracefully and display helpful error messages.

## Usage
1. Customize the `URL` variable in the script to point to your preferred source of COVID-19 statistics.
2. Run the script using the instructions provided above.
3. The script will fetch the latest data and notify you with statistics for each state or region.

## Configuration
- The script can be easily configured by adjusting the `URL` variable and the path to the notification icon (`ICON_PATH`) to suit your needs.

## License
- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project uses the `plyer` library for sending desktop notifications and the `requests` library for making HTTP requests.

Feel free to modify and use this script to stay updated on COVID-19 statistics. If you have any questions or suggestions, please don't hesitate to reach out.

