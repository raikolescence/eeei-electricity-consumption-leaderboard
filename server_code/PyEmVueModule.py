# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import anvil.server

# import datetime
# import time
# from pyemvue.pyemvue import PyEmVue
# from pyemvue.enums import Scale, Unit
# import copy

# # This is a server module. It runs on the Anvil server,
# # rather than in the user's browser.
# #
# # To allow anvil.server.call() to call functions here, we mark
# # them with @anvil.server.callable.
# # Here is an example - you can replace it with your own:
# #
# # @anvil.server.callable
# # def say_hello(name):
# #   print("Hello, " + name + "!")
# #   return 42
# #

# # pyemvue start

# lab_a_base = [[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95],[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95],[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95],[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95],[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95],[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95],[0.28, 0.67, 0.81, 0.09, 0.65, 0.12, 0.64, 38.48, 45.57, 54.61, 12.84, 16.89, 53.87, 46.32, 11.49, 12.67, 41.62, 52.30, 40.46, 29.38, 0.42, 0.03, 0.17, 0.95]]
# lab_b_base = [[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92],[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92],[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92],[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92],[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92],[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92],[0.43, 0.63, 0.95, 0.63, 0.47, 0.06, 0.28, 58.31, 57.64, 27.54, 49.70, 22.46, 22.57, 47.68, 10.56, 58.59, 30.98, 13.93, 36.64, 51.73, 0.69, 0.45, 0.50, 0.92]]
# lab_c_base = [[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96],[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96],[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96],[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96],[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96],[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96],[1.00, 0.48, 0.73, 0.91, 0.30, 0.96, 0.81, 55.43, 56.78, 28.98, 46.84, 54.02, 55.38, 13.99, 11.16, 45.18, 24.24, 14.87, 36.71, 44.91, 0.36, 0.25, 0.16, 0.96]]
# lab_d_base = [[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70],[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70],[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70],[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70],[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70],[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70],[0.19, 0.86, 0.79, 0.48, 0.15, 0.19, 0.14, 28.96, 58.12, 30.55, 35.26, 41.26, 59.04, 26.35, 50.61, 38.24, 22.04, 51.25, 32.88, 52.40, 0.99, 0.29, 0.44, 0.70]]

# class Lab:
#   def __init__(self, name, baseline, gid, channel, overuse_threshold=2):
#       self.name = name
#       self.baseline = baseline
#       self.gid = gid
#       self.channel = channel
#       self.current = []
#       self.sum_baseline = []
#       self.sum_current = []
#       self.difference = []          
#       self.overuse_threshold = overuse_threshold  # set the threshold for consecutive overuse
#       self.overuse_counter = 0  # initialize counter for consecutive overuse

#   def input_current_consumption(self, hour):
#       consumption = float(input(f"Enter current consumption for {self.name}: "))
#       self.current.append(consumption)

#   def update_differences(self):
#       now = datetime.datetime.now()
#       day_of_week = now.weekday()  # Monday is 0 and Sunday is 6
#       hour_of_day = now.hour

#       # Ensure lists are of adequate size for today
#       required_size = hour_of_day + 1
#       self.ensure_list_size(self.sum_baseline, required_size)
#       self.ensure_list_size(self.sum_current, required_size)
#       self.ensure_list_size(self.difference, required_size)

#       if day_of_week < len(self.current):
#           cumulative_current = 0
#           cumulative_baseline = 0
#           for hour in range(hour_of_day + 1):
#               current_consumption = self.current[day_of_week][hour] if hour < len(self.current[day_of_week]) else 0
#               baseline_consumption = self.baseline[day_of_week][hour] if hour < len(self.baseline[day_of_week]) else 0
#               cumulative_current += current_consumption
#               cumulative_baseline += baseline_consumption
#               # Update the sums and differences for each hour up to the current hour
#               self.sum_current[hour] = cumulative_current
#               self.sum_baseline[hour] = cumulative_baseline
#               self.difference[hour] = current_consumption - baseline_consumption
#       else:
#           print(f"No current consumption data available for {self.name} on day {day_of_week} up to hour {hour_of_day}")

#   def ensure_list_size(self, list_to_check, required_size):
#       while len(list_to_check) < required_size:
#           list_to_check.append(0)
#   def print_differences(self):
#       # Ensure differences are updated before printing
#       self.update_differences()

#       print(f"Differences for {self.name}:")
#       print(self.sum_current)
#       print(self.sum_baseline)
#       print(self.difference)
  
#   def compare_consumption(self):
#       current_time = datetime.datetime.now()
#       day_of_week = current_time.weekday()  # 0 is Monday, 6 is Sunday
#       hour_of_day = current_time.hour

#       # Round up the time to the next hour if needed
#       if current_time.minute >= 30:
#           hour_of_day = (hour_of_day + 1) % 24

#       if day_of_week < len(self.current) and hour_of_day < len(self.current[day_of_week]):
#           current_consumption = self.current[day_of_week][hour_of_day]
#           baseline_consumption = self.baseline[day_of_week][hour_of_day]

#           if baseline_consumption < 1 and current_consumption > 2 or current_consumption > 1.5 * baseline_consumption:
#               self.overuse_counter += 1
#               if self.overuse_counter >= self.overuse_threshold:
#                   print(
#                       f"Alert: {self.name} is using too much power at hour {hour_of_day} for {self.overuse_threshold} consecutive times.")
#                   app_tables.alertserrors.add_row(Time=datetime.datetime.now(), Alerts=f"Alert: {self.name} is using too much power at hour {hour_of_day} for {self.overuse_threshold} consecutive times.")
#               else:
#                   # Print warning without triggering the alert counter
#                   print(f"Warning: {self.name} is using too much power at hour {hour_of_day}.")
#                   app_tables.alertserrors.add_row(Time=datetime.datetime.now(), Alerts=f"Warning: {self.name} is using too much power at hour {hour_of_day}.")
#           else:
#               self.overuse_counter = 0  # Reset counter if the condition doesn't meet
#   def compare_consumption_manual(self, day_of_week, hour):
#       if day_of_week < len(self.current) and hour < len(self.current[day_of_week]):
#           current_consumption = self.current[day_of_week][hour]
#           baseline_consumption = self.baseline[day_of_week][hour]

#           # Logic to check overuse based on the threshold
#           if baseline_consumption < 1 and current_consumption > 2 or current_consumption > 1.5 * baseline_consumption:
#               self.overuse_counter += 1
#               if self.overuse_counter >= self.overuse_threshold:  # Use the dynamic threshold
#                   print(
#                       f"Alert: {self.name} is using too much power at hour {hour} for {self.overuse_threshold} consecutive times.")
#                   app_tables.alertserrors.add_row(Time=datetime.datetime.now(), Alerts=f"Alert: {self.name} is using too much power at hour {hour} for {self.overuse_threshold} consecutive times.")
#           else:
#               self.overuse_counter = 0  # Reset counter if the condition doesn't meet

#   #@staticmethod
#   def calculate_percentage_difference(current_sum, baseline_sum):
#       return (current_sum - baseline_sum) / baseline_sum * 100



# """    def input_current_consumption(self, sensor_gid, vue):
#       end_time = datetime.datetime.now(datetime.timezone.utc)
#       start_time = end_time - datetime.timedelta(minutes=15)
#       usage_over_time, start_time = vue.get_chart_usage(sensor_gid, start_time, end_time, scale=Scale.MINUTE.value, unit=Unit.KWH.value)

#       total_usage = sum(usage_over_time)
#       self.current.append(total_usage)"""

# def input_current_consumption(self, sensor_gid, vue):
#       devices = vue.get_devices()
#       channel = None

#       # Find the channel that matches the sensor_gid
#       for device in devices:
#           if device.device_gid == sensor_gid:
#               channel = device.channels[0]
#               break

#       if channel:
#           end_time = datetime.datetime.now(datetime.timezone.utc)
#           start_time = end_time - datetime.timedelta(minutes=1)
#           usage_over_time, start_time = vue.get_chart_usage(channel, start_time, end_time, scale=Scale.MINUTE.value,
#                                                             unit=Unit.KWH.value)

#           if usage_over_time:
#               total_usage_1_minute = (sum(usage_over_time) / 2) * 1000  # kWh to Watts conversion
#               self.current.append(total_usage_1_minute)
#           else:
#               print(f"No data available for sensor GID: {sensor_gid}")
#               app_tables.alertserrors.add_row(Time=datetime.datetime.now(), Alerts=f"No data available for sensor GID: {sensor_gid}")
#       else:
#           print(f"Device with GID {sensor_gid} not found")
#           app_tables.alertserrors.add_row(Time=datetime.datetime.now(), Alerts=f"Device with GID {sensor_gid} not found")


# def arrange_function(rankings):
#   for i in range(len(rankings)):
#       for j in range(i + 1, len(rankings)):
#           if (rankings[i][1]) > (rankings[j][1]):
#               # Swap
#               rankings[i], rankings[j] = rankings[j], rankings[i]


# def initialize_current_consumption_with_baseline(lab_instance, baseline_data):
#   lab_instance.current = copy.deepcopy(baseline_data)


# def update_lab_current_consumption(lab, total_consumption):

#   current_time = datetime.datetime.now()
#   day_of_week = current_time.weekday()  # 0 is Monday, 6 is Sunday

#   while len(lab.current) <= day_of_week:
#       lab.current.append([0] * 24)  # Initialize with zeroes for each hour

#   hour_of_day = current_time.hour  # 0 to 23


#   lab.current[day_of_week][hour_of_day] = total_consumption

# def sum_consumption_and_baseline(labs):
#   # Get the current time details
#   now = datetime.datetime.now()
#   day_of_week = now.weekday()  # Monday is 0 and Sunday is 6
#   hour_of_day = now.hour

#   # Initialize the sums
#   total_current_consumption = 0
#   total_baseline_consumption = 0

#   # Iterate through each lab
#   for lab in labs:
#       # Sum the consumption from the start of the week to the current hour today
#       for day in range(day_of_week + 1):  # Include today
#           if day < day_of_week:  # Full day
#               total_current_consumption += sum(lab.current[day])
#               total_baseline_consumption += sum(lab.baseline[day])
#           else:  # Today, sum up to the current hour
#               total_current_consumption += sum(lab.current[day][:hour_of_day + 1])
#               total_baseline_consumption += sum(lab.baseline[day][:hour_of_day + 1])

#   # Calculate the difference
#   difference = total_current_consumption - total_baseline_consumption

#   print(f"Total current consumption from all labs: {total_current_consumption}")
#   print(f"Total baseline consumption from all labs: {total_baseline_consumption}")
#   print(f"Difference between total consumption and baseline: {difference}")

#   return total_current_consumption, total_baseline_consumption, difference

# def battle(lab1, lab2, rankings):
#   current_time = datetime.datetime.now()
#   day_of_week = current_time.weekday()  # 0 is Monday, 6 is Sunday
#   hour_of_day = current_time.hour +1

#   # Round up the time to the next hour for summation
#   if current_time.minute >= 30:
#       hour_of_day += 1
#   print(hour_of_day)
#   # Ensure hour_of_day does not exceed 23 (max index for hourly data)
#   hour_of_day = min(hour_of_day, 23)

#   # Sum up to the current (or next, if rounded up) hour
#   sum_current_1 = sum(lab1.current[day_of_week][:hour_of_day])
#   sum_baseline_1 = sum(lab1.baseline[day_of_week][:hour_of_day])
#   print(sum_current_1)
#   print(sum_baseline_1)
#   sum_current_2 = sum(lab2.current[day_of_week][:hour_of_day])
#   sum_baseline_2 = sum(lab2.baseline[day_of_week][:hour_of_day])

#   percent_diff_1 = Lab.calculate_percentage_difference(sum_current_1, sum_baseline_1)
#   percent_diff_2 = Lab.calculate_percentage_difference(sum_current_2, sum_baseline_2)

#   rankings.append([lab1.name, percent_diff_1])
#   rankings.append([lab2.name, percent_diff_2])

#   winner = lab1.name if percent_diff_1 < percent_diff_2 else lab2.name
#   print(f"The winner is {winner}.")
#   print(f"Difference between {lab1.name} and baseline: {percent_diff_1:.2f}%")
#   print(f"Difference between {lab2.name} and baseline: {percent_diff_2:.2f}%")
#   app_tables.matches.add_row(battle_time=datetime.datetime.now(), battle_winner=winner, participant1=lab1.name,participant1_score=percent_diff_1, participant2=lab2.name ,participant2_score=percent_diff_2)


# # def save_lab_current_to_file(labs, folder_path):
# #     # Ensure the folder exists
# #     if not os.path.exists(folder_path):
# #         os.makedirs(folder_path)

# #     file_path = os.path.join(folder_path, "lab_consumption_data.txt")

# #     with open(file_path, "a") as file:
# #         # date
# #         file.write(f"Update Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
# #         for lab in labs:
# #             # name
# #             file.write(f"{lab.name} current consumption: {lab.current}\n")
# #         file.write("\n")

# def sum_and_compare_each_lab(labs):
#   # Iterate through each lab
#   for lab in labs:
#       if lab.sum_current and lab.sum_baseline:
#           # Fetch the last updated values for current and baseline consumption
#           lab_current_consumption = lab.sum_current[-1]
#           lab_baseline_consumption = lab.sum_baseline[-1]
#           difference = lab_current_consumption - lab_baseline_consumption
#           percent_difference = (difference / lab_baseline_consumption * 100) if lab_baseline_consumption != 0 else float('inf')

#           # Print the results for this lab
#           print(f"Lab {lab.name}:")
#           print(f"  Current consumption up to now: {lab_current_consumption}")
#           print(f"  Baseline consumption up to now: {lab_baseline_consumption}")
#           print(f"  Difference: {difference}")
#           print(f"  Percentage difference: {percent_difference:.2f}%\n")
#       else:
#           print(f"Data for {lab.name} is incomplete or not updated.")  

# def get_total_lab_consumption(vue, lab, time_delta_minutes):
#   while True:
#       try:
#           total_consumption = 0
#           end_time = datetime.datetime.now(datetime.timezone.utc)
#           start_time = end_time - datetime.timedelta(minutes=time_delta_minutes)

#           # Attempt to get devices, this might fail if the WiFi is down
#           devices = vue.get_devices()

#           for gid, channel_num in zip(lab.gid, lab.channel):
#               for device in devices:
#                   if device.device_gid == gid:
#                       for channel in device.channels:
#                           if str(channel.channel_num) == str(channel_num):
#                               channel_usage, _ = vue.get_chart_usage(
#                                   channel,
#                                   start_time,
#                                   end_time,
#                                   scale=Scale.MINUTE.value,
#                                   unit=Unit.KWH.value
#                               )
#                               if channel_usage:
#                                   total_consumption += sum(channel_usage)
#                               break
#           return total_consumption
#       except (ConnectionError, requests.exceptions.RequestException) as e:
#           print(f"Connection error: {e}. Retrying in 5 seconds...")
#           app_tables.alertserrors.add_row(Time=datetime.datetime.now(), Error=f"Connection error: {e}. Retrying in 5 seconds...")
#           time.sleep(5)


# def calculate_all_labs_consumption(vue, labs, time_delta_minutes):
#   consumption_dict = {}
#   for lab in labs:
#       consumption = get_total_lab_consumption(vue, lab, time_delta_minutes)
#       consumption_dict[lab.name] = consumption
#   return consumption_dict


# # Define function to update the database with rankings
# def update_database_with_rankings(rankings):
#     # Get the current timestamp
#     timestamp = datetime.datetime.now()

#     # Iterate through the rankings and update the database table
#     for lab in rankings:
#         lab_row = app_tables.labs.get(name=lab[0])
#         print(lab, lab_row)
#         lab_row['LastSavingsValue'] = lab[1]
#         lab_row['TotalSavings'] = lab[1] + lab_row['TotalSavings']
#         lab_row['TotalSavingsLastUpdated'] = timestamp
#         lab_row['TotalSavingsUpdateCount'] = lab_row['TotalSavingsUpdateCount'] + 1
      

#     rankings = []  # restart rankings"""

# @anvil.server.callable
# def update_weekly_database():
#   if len(app_tables.weeklydata.search()) > 6:
#     app_tables.weeklydata.search()[0].delete()
#     app_tables.weeklydata.add_row(timestamp=datetime.datetime.now(), CNL=1, Microlab=1, RAL=1, SSL=1)
#   else:
#     app_tables.weeklydata.add_row(timestamp=datetime.datetime.now(), CNL=1, Microlab=1, RAL=1, SSL=1)


# @anvil.server.background_task
# # @anvil.server.callable
# def run_pyemvue():
  
#   lab_a = Lab("Smart Systems Laboratory", lab_a_base, [169101],[1])
#   lab_b = Lab("COMPUTER NETWORKS LABORATORY", lab_b_base, [175618],[1])
#   lab_c = Lab("Microelectronics and Microprocessors Laboratory", lab_c_base, [175619,169101],[1,1])
#   lab_d = Lab("Robotics Automation Laboratory", lab_d_base, [228886],[1])
#   labs = [lab_a,lab_b,lab_c,lab_d]
#   rankings = []
  
  
#   vue = PyEmVue()
#   vue.login(username='rqorosco@up.edu.ph', password='Password123!!!')
#   # Main loop
#   devices = vue.get_devices()
  
#   device_consumptions = []
  
#   initialize_current_consumption_with_baseline(lab_a, lab_a_base)
#   initialize_current_consumption_with_baseline(lab_b, lab_b_base)
#   initialize_current_consumption_with_baseline(lab_c, lab_c_base)
#   initialize_current_consumption_with_baseline(lab_d, lab_d_base)
  
#   lab_consumptions = {}
#   time_delta_minutes = 60  # The time delta in minutes for which you want to check the consumption
  
#   for lab in labs:
#     lab_consumptions[lab.name] = get_total_lab_consumption(vue, lab, time_delta_minutes)
  
#   # Print the total consumptions
#   print(lab_consumptions)
  
#   app_tables.data.add_row(**lab_consumptions, DataLastUpdate=datetime.datetime.now())
  
#   print(lab_a.current)
#   print(lab_b.current)
#   print(lab_c.current)
#   print(lab_d.current)

#   device_consumptions = []
#   summed_device_consumptions = {}

#   for lab in labs:
#       summed_device_consumptions[lab.name] = get_total_lab_consumption(vue, lab, time_delta_minutes)

#   # Print the total consumptions
#   print(summed_device_consumptions)

#   # Update current consumption for each lab using summed values
#   for lab in labs:
#       total_consumption = summed_device_consumptions[lab.name]
#       update_lab_current_consumption(lab, total_consumption)

#   print(lab_a.current)
#   print(lab_a.baseline)
#   print(lab_b.current)
#   print(lab_c.current)
#   print(lab_d.current)


#   lab_a.compare_consumption()
#   lab_b.compare_consumption()
#   lab_c.compare_consumption()
#   lab_d.compare_consumption()

#   battle(lab_a, lab_b, rankings)
#   battle(lab_c, lab_d, rankings)
#   arrange_function(rankings)

#   print("Rankings:", rankings)

#   # Update database with rankings
#   update_database_with_rankings(rankings)

