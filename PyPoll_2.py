{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "25400c13-35ad-4197-b0d5-1743a3a861d0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Charles Casper Stockham: 23.049%\n",
      "Diana DeGette: 73.812%\n",
      "Raymon Anthony Doane: 3.139%\n",
      "Election Results\n",
      "-----------------------\n",
      "Total Votes: 369711\n",
      "-----------------------\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "Diana DeGette: 73.812% (272892)\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "-----------------------\n",
      "The winning candidate is Diana DeGette with 272892 votes.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Initialize variables to keep track of the winning candidate and their vote count\n",
    "winning_candidate = \"\"\n",
    "winning_count = 0\n",
    "\n",
    "# Create a formatted string to store all candidate results\n",
    "candidate_results = \"\"\n",
    "\n",
    "# Iterate through each candidate in candidate_votes dictionary\n",
    "for candidate in candidate_votes:\n",
    "    candidate_vote_count = candidate_votes[candidate]\n",
    "    \n",
    "    # Calculate the vote percentage for the current candidate\n",
    "    vote_percentage = (candidate_vote_count / total_votes) * 100\n",
    "    \n",
    "    # Print the candidate's name and their vote percentage with 3 decimal places\n",
    "    print(f\"{candidate}: {vote_percentage:.3f}%\")\n",
    "    \n",
    "    # Check if the current candidate has more votes than the current winning_count\n",
    "    if candidate_vote_count > winning_count:\n",
    "        winning_count = candidate_vote_count\n",
    "        winning_candidate = candidate\n",
    "    \n",
    "    # Create a formatted string to display the candidate's name, vote percentage, and vote count\n",
    "    voter_output = f\"{candidate}: {vote_percentage:.3f}% ({candidate_vote_count})\"\n",
    "    \n",
    "    # Append the candidate's results to the overall candidate_results string\n",
    "    candidate_results += voter_output + \"\\n\"\n",
    "\n",
    "# Write the election analysis results to the text file\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    election_results = (\n",
    "        f\"Election Results\\n\"\n",
    "        f\"-----------------------\\n\"\n",
    "        f\"Total Votes: {total_votes}\\n\"\n",
    "        f\"-----------------------\\n\"\n",
    "        f\"{candidate_results}\"\n",
    "        f\"-----------------------\\n\"\n",
    "        f\"The winning candidate is {winning_candidate} with {winning_count} votes.\\n\"\n",
    "    )\n",
    "\n",
    "    print(election_results)\n",
    "    txt_file.write(election_results)\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52be6a86-9cec-4ee0-8534-23db85317f3d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2e6ace4-c93c-49e9-81bf-6dbb4324e8e0",
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
