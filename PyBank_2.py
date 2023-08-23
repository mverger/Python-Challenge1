{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "876b49ea-2a03-4ccf-83f1-392a5d68774b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-1443517, 631156, -1004755, 1581126, -289272, -1098929, 1167557, -806093, 1124485, -1736491, -408383, 604557, -294345, 1327485, 394323, 243585, -617439, -1530577, 1390390, -1130397, 1293604, 641758, -337413, -52031, -937192, 863841, -76245, -100481, -960729, 591856, 54930, 680102, -250254, -840415, 582358, -48628, -135256, 978586, -599210, -442789, 652924, -1005714, 1167373, -234900, -165147, -52275, -302320, 719028, -1825558, 1287083, -48303, 210234, -236414, 585165, -1400632, 839777, 465229, 317811, -760202, -71868, 795457, -182685, -1242836, 1371884, -445193, 10025, -1043998, 1350395, 80538, -1223250, 104148, 843924, -1808664, 1505005, 306402, -143603, -1266937, -162519, 1862002, -52986, -1627245, 616795, 628522, 90895, -224669]\n",
      "['Aug-16', 1862002]\n",
      "['Feb-14', -1825558]\n",
      "Financial Analysis\n",
      "--------------------------------\n",
      "Total Months: 86\n",
      "Total: $22564198\n",
      "Average Change $-8311.105882352942\n",
      "Greatest Increase in Profits: Aug-16 ($1862002)\n",
      "Greatest Decrease in Profits: Feb-14 ($-1825558)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "#file to load and output\n",
    "\n",
    "file_to_load = os.path.join(\".\", \"Resources\", \"budget_data.csv\")\n",
    "file_to_load\n",
    "file_to_output = os.path.join(\".\", \"budget_analysis.txt\")\n",
    "\n",
    "total_months = 0\n",
    "total_net = 0\n",
    "net_change_list = []\n",
    "month_of_changes = []\n",
    "\n",
    "greatest = [\"\", 0]\n",
    "least = [\"\", 1000000000000000000000000]\n",
    "\n",
    "# Read the csv and convert to list\n",
    "with open(file_to_load) as financial_data:\n",
    "   \n",
    "    reader = csv.reader(financial_data)\n",
    "        \n",
    "        \n",
    "    # Skip header row\n",
    "    header = next(reader)\n",
    "    \n",
    "    #print(f\"Header: {header}\")\n",
    "    first_row = next(reader)\n",
    "    \n",
    "    total_net += int(first_row[1])\n",
    "    \n",
    "    previous_net = int(first_row[1])\n",
    "    \n",
    "    total_months += 1\n",
    "    \n",
    "    for row in reader:\n",
    "        \n",
    "        #total_months = total_months +1\n",
    "        total_months += 1\n",
    "        total_net += int(row[1])\n",
    "        \n",
    "        # Track net change\n",
    "        net_change = int(row[1]) - previous_net\n",
    "        previous_net = int(row[1])\n",
    "        net_change_list.append(net_change)\n",
    "        \n",
    "        # Calculate greatest increase\n",
    "        if(net_change > greatest[1]): \n",
    "            greatest[0] = row[0]\n",
    "            greatest[1] = net_change\n",
    "            \n",
    "        # Calculate greatest decrease\n",
    "        if(net_change < least[1]): \n",
    "            least[0] = row[0]\n",
    "            least[1] = net_change\n",
    "        \n",
    "print(net_change_list)\n",
    "\n",
    "print(greatest)\n",
    "print(least)\n",
    "net_monthly_average = sum(net_change_list)/ len(net_change_list)\n",
    "\n",
    "\n",
    "output = (\n",
    "    f\"Financial Analysis\\n\"\n",
    "    f\"--------------------------------\\n\"\n",
    "    f\"Total Months: {total_months}\\n\"\n",
    "    f\"Total: ${total_net}\\n\"\n",
    "    f\"Average Change ${net_monthly_average}\\n\"\n",
    "    f\"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\\n\"\n",
    "    f\"Greatest Decrease in Profits: {least[0]} (${least[1]})\"\n",
    ")\n",
    "\n",
    "print(output)\n",
    "\n",
    "#Financial Analysis\n",
    "#--------------------------\n",
    "# Total months = 86\n",
    "#Total: $22564198\n",
    "#Avg Change: $-8311.11\n",
    "#Greatest Incr in Profits: Aug 16 $1862002\n",
    "#Greatest Decr in Profits: Feb 14 $-1825558\n",
    "\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    txt_file.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48511f03-9f80-4749-ae16-94963cf890b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "add699dd-ee63-41e0-95b9-e7edcffe6734",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58be8a6e-62e7-42a0-8c40-ada63a78722f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
