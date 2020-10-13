# Streetwise scoring

This is a script using a pre-trained neural network (see [1]) to predict the perceived safety score of a certain place in a city.
The NN model compares pairs of images and estimates which one is taken in the safest place. This information is then used to compute the TrueSkill score [2] using the TrueSkill package [3]. The results are then exported in the GeoJSON format [4].

### Results

Sample results can be found in the ```safety_scores``` folder. These can be easily visualized, for example using mapbox:

- [<img src="https://github.com/Streetwise/streetwise-score/blob/master/wiki_images/romanshorn.png" alt="Romanshorn" width="500px"/>](https://api.mapbox.com/styles/v1/colombmo/ckesny6m30o9019p97rv594qx.html?fresh=true&title=view&access_token=pk.eyJ1IjoiY29sb21ibW8iLCJhIjoiY2tlYTE5MmpvMTB6cTJxcm41Ynl1OTNxYSJ9.6SsIy1FTpxao9Sv-hvRDSg)
- [<img src="https://github.com/Streetwise/streetwise-score/blob/master/wiki_images/luzern.png" alt="Luzern" width="500px"/>](https://api.mapbox.com/styles/v1/colombmo/ckeskgshq764k19o21zu3l7fw.html?fresh=true&title=view&access_token=pk.eyJ1IjoiY29sb21ibW8iLCJhIjoiY2tlYTE5MmpvMTB6cTJxcm41Ynl1OTNxYSJ9.6SsIy1FTpxao9Sv-hvRDSg)
- [<img src="https://github.com/Streetwise/streetwise-score/blob/master/wiki_images/stgallen.png" alt="St. Gallen" width="500px"/>](https://api.mapbox.com/styles/v1/colombmo/ckesiukh124lb19mt27xeg56r.html?fresh=true&title=view&access_token=pk.eyJ1IjoiY29sb21ibW8iLCJhIjoiY2tlYTE5MmpvMTB6cTJxcm41Ynl1OTNxYSJ9.6SsIy1FTpxao9Sv-hvRDSg)
- [<img src="https://github.com/Streetwise/streetwise-score/blob/master/wiki_images/schaffhausen.png" alt="Schaffhausen" width="500px"/>](https://api.mapbox.com/styles/v1/colombmo/cketssk0r91th19qq2l9jcd3h/draft.html?fresh=true&title=view&access_token=pk.eyJ1IjoiY29sb21ibW8iLCJhIjoiY2tlYTE5MmpvMTB6cTJxcm41Ynl1OTNxYSJ9.6SsIy1FTpxao9Sv-hvRDSg)


### References

[1] https://github.com/Streetwise/streetwise-data/wiki/MachineLearning

[2] Herbrich, R., Minka, T. and Graepel, T., 2007. TrueSkill™: a Bayesian skill rating system. In _Advances in neural information processing systems_ (pp. 569-576).

[3] https://trueskill.org/

[4] https://geojson.org/
