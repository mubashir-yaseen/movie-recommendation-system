# Recommendation System

## Overview
This project implements a recommendation system using collaborative filtering techniques. It analyzes user-item interactions to generate personalized recommendations for users.

## Project Website
Check out the live demo of the recommendation system [here](https://recommendation-sys-uy0j.onrender.com).

## Features
- Collaborative filtering based on user-item interactions.
- Recommendation generation for users.
- Evaluation metrics to assess recommendation quality.
- User feedback for refining recommendations.

## Getting Started
### Prerequisites
- Python 3.x
- Required packages listed in `requirements.txt`. Install them using:
pip install -r requirements.txt

### Installation
1. Clone the repository:
git clone https://github.com/mubashir-yaseen/recommendation_sys.git

2. Navigate to the project directory:
cd recommendation_sys

### Usage
1. Train the recommendation system:
python train.py

2. Generate recommendations:
python recommend.py

3. Collecting User Feedback:
To collect user feedback, follow these steps:
- Run the application by executing:
  ```
  python app.py
  ```
- Visit the application in your web browser.
- Select a movie from the dropdown list and click "Get Recommendations".
- Review the recommended movies and click either "Like" or "Dislike" for each movie to provide feedback.

### Evaluation
Evaluate the recommendation system using evaluation metrics:
python evaluate.py

## Dataset
The project includes a sample dataset (`data.csv`) containing user-item interactions for demonstration purposes. This dataset was downloaded from [Kaggle](https://www.kaggle.com/), a platform for data science and machine learning competitions, challenges, and datasets. You can find the dataset used in this project on the Kaggle dataset page [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [STANFORD eBook](http://infolab.stanford.edu/~ullman/mmds/ch9.pdf)
- [STANFORD Research Paper](https://cs229.stanford.edu/proj2013/Bystrom-MovieRecommendationsFromUserRatings.pdf)
- [MIT Research Paper](https://news.mit.edu/2011/compare-recommendation-systems-0708)
- [IEEE Research Paper](https://ieeexplore.ieee.org/document/8663822)

## Contact
For any questions or feedback, feel free to reach out:
- Email: mubashir_yaseen@hotmail.com
- LinkedIn: https://www.linkedin.com/in/muhammad-mubashir-38a1361a1/
