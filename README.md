# Streetwise scoring

This is a script using a pre-trained neural network (see [1]) to predict the perceived safety score of a certain place in a city.
The NN model compares pairs of images and estimates which one is taken in the safest place. This information is then used to compute the TrueSkill score [2] using the TrueSkill package [3]. The results are then exported in the GeoJSON format [4].

### Results

Sample results can be found in the ```safety_scores``` folder. These can be easily visualized, for example using mapbox:

- 


### References

[1] https://github.com/Streetwise/streetwise-data/wiki/MachineLearning

[2] Herbrich, R., Minka, T. and Graepel, T., 2007. TrueSkill™: a Bayesian skill rating system. In _Advances in neural information processing systems_ (pp. 569-576).

[3] https://trueskill.org/

[4] https://geojson.org/
