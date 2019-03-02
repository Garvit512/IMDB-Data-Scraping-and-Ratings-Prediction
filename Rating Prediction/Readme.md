# Rating prediction procedure:-

##NOTE-  
Each step performed in the prediction is mentioned in the code (i.e .ipynb file) for proper understanding and for view .ipynb file, please install [jupyter notebook](https://jupyter.org/).

**Step-1:**
importing essential libraries like pandas, numpy, matplotlib e.t.c

**Step-2:** 
>Feature Selection & data preprocessing

 Visualize independent variables like Budget, Revieweres, Genre for finding the impact of each independent variable on the ratings (dependent variable).
Then selecting the features which have higher impact on ratings comparatively to others.
Some fields have null values because those data are not available on website so for Budget, null values are replaced with 0 (zero) because replacing null values with mean of Budget or something else would not work because there are many movies which are too high in budget and also some are too low.

**Step-3:** >Converting categorical data into numericals:-
We can’t apply prediction or any algorithm on text (categorical) data because machine can’t process text so we’ve to convert text into vectors (numbers) for proper machine understanding.

**Step-4:** >Feature Scaling:-
It is a good practice to scale the values into one standard so that the algorithm will give more accurate results and there should be no biasing.
Step-5 -> Model Building (Prediction):-
This is the last step in which we feed all the selected features and resultant data into the algorithm to predict the rating.
Problem-  In the data most movies have rating in the range of 8.0 to 8.9 and we’ve trained our algorithm with same data so in some cases, the algorithm may give incorrect results for the movies having rating below 8.
We’ve applied Linear Regression  to predict the rating of the movies because other methods encountering underfitting and overfittting issues.
