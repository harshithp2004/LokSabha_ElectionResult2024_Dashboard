# LokSabha_ElectionResult2024_Dashboard
## Total Constituency, Total Candidates, Total Political Parties, Average Margin Victory (Top Section):
Question: How many constituencies, candidates, and political parties are represented in the 2024 Lok Sabha elections, and what is the average margin of victory across constituencies?
Conclusion: The dashboard reports 543 constituencies, with 1083 candidates competing across 63 political parties. The average margin of victory stands at 162.05K votes, giving an overview of the election's scale and competitiveness.

## Status Filter (Result Declared, Uncontested):
Question: What election result statuses can be filtered in the dashboard?
Conclusion: Users can filter constituencies based on whether the result is declared or if the constituency was uncontested, allowing focused analysis on specific outcomes.

## Total Seats by Each Party (Bar Chart):
Question: How are the total seats distributed among the leading political parties in the 2024 Lok Sabha elections?
Conclusion: The Bharatiya Janata Party (BJP) holds the most seats, with over 200 constituencies. The Indian National Congress follows, while other parties like Samajwadi Party, All India Trinamool Congress, and Dravida Munnetra Kazhagam secure fewer seats. This shows the dominance of BJP in the elections.

## Margin Distribution by Leading Party (Bar Chart):
Question: What is the distribution of victory margins across various constituencies, and which parties have the largest margins?
Conclusion: The chart reveals the constituencies with the largest victory margins. Constituencies like Indore and Vidisha have the highest margins, primarily represented by the BJP. There is significant variation in margins across constituencies, indicating that some areas experienced landslides, while others were more closely contested.

## Constituency Distribution by Leading Party (Map):
Question: How are constituencies distributed geographically across India based on the leading political party?
Conclusion: The map visualizes the geographic distribution of constituencies and the leading parties. Constituencies led by major parties such as the BJP and Congress are spread throughout India, providing a spatial understanding of party dominance across regions.

## Detailed View (Table):
Question: What are the details of leading candidates, leading parties, and constituencies in the 2024 Lok Sabha elections?
Conclusion: The table provides detailed information on the leading candidate and leading party for each constituency. For example, Godam Nagesh is the leading candidate in Adilabad, representing the BJP, while other candidates like Prof S P Singh Baghel lead in Agra, also representing the BJP. This offers granular insight into individual results.

## Overall Conclusion:
The 2024 Lok Sabha Election Dashboard provides a comprehensive view of the election outcomes, with insights into seat distribution, victory margins, constituency distribution, and details on leading candidates and parties. The BJP dominates the elections in terms of total seats and victory margins, while the map and detailed view help in understanding the geographic and candidate-level dynamics.

# Machine Learning Insights
## Code:
<a href="https://github.com/harshithp2004/LokSabha_ElectionResult2024_Dashboard/blob/main/ml_integrated_LokSabha2024.py">ml_integrated_LokSabha2024</a>

## Objective of Use of ML:
What are the relative importances of the features 'Constituency Number' and 'Margin' in predicting the election results or influencing a model's outcome?
Conclusion:
The chart shows that Margin has the highest feature importance, with a relative importance close to 1 (almost 100%), indicating that this variable is the most significant predictor in the model or analysis.On the other hand, Constituency Number has very low importance, suggesting that this feature contributes very little to the prediction or result compared to the margin.
