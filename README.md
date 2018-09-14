# NFL-ExpectedPoints-Ratings
This repository includes the code for obtaining NFL team ratings in terms of expected points. The method is described in our work: "Evaluating NFL plays: Expected points adjusted for schedule"


We use the data from the nflscrapR package. For every season, we separate:

1. passing
2. rushing
3. special teams (includes punts and kickoffs together)

Given the expected points added for every play, we calculate offensive and defensive ratings for a team for each one of the play types. For special teams, offense is consider the team that punts/kickoffs (i.e., coverage), while the defense is considered the team that returns the punt/kickoff.

The optimization described in our paper essentially obtains a team rating. E.g., a team with an offensive passing rating of 0.1 means that is 0.1 expected points per play better than average (an average team has a rating of 0). Similarly a team with a defensive rating of 0.1 means that it allows 0.1 expected points per play more than an average team (so for defensive rating a negative value is better!). These ratings take into consideration the opposition strength every team faced.
