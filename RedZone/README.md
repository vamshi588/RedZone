**Accident Hotspot AI: Predict Road Accidents Before They Happen!**

What if we could spot dangerous road spots before an accident happens?
This project uses AI + real-world data to do just that!
This project is a blend of:
Road network data
Past accident records
Weather conditions
Machine learning magic

**The goal?** Help cities prevent crashes rather than just reacting to them.

**What’s Inside?**

accident_hotspot_ai/

├── data/             # Input datasets (accidents, weather, roads)

├── models/           # Trained AI models

├── outputs/          # Maps, reports

├── src/              # All the code (modular and clean)

├── main.py           # Runs the full pipeline

├── requirements.txt  # Dependencies

└── README.md         # You're reading it!

**How does it work?**

The pipeline:

Load real-world accident, weather, and road data

Generate synthetic “safe” points for training

Engineer smart features (hour, day, rain, etc.)

Train a machine learning model (Random Forest)

Map predicted hotspots

**Quickstart**

Clone + set up:

git clone https://github.com/chin0308/accident-hotspot-ai.git

cd accident-hotspot-ai

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt


**Drop your data in the data/ folder:**

Motor_Vehicle_Collisions_-_Crashes.csv

open-meteo-52.54N13.36E38m.csv

export.geojson


**Run it:**

python main.py

It will save your model as models/accident_rf.pkl.

Create an interactive map named outputs/prediction_map.html.

Open the map in your browser and see where risk zones light up!


**Data Sources:**

[NYC Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)

[Open-Meteo (historical weather)](https://open-meteo.com/en/docs/gfs-api)

[OpenStreetMap (roads)](https://overpass-turbo.eu/)


**Why is this cool?**

Combines traffic, weather + road data

Generates “non-accident” training points automatically

Outputs a real map showing risk zones

Easy to extend (GNNs, real-time feeds, dashboards!)


**Where can this be taken?**

Add graph neural networks for better spatial learning

Build a Streamlit app or dashboard

Plug into real-time data streams for live prediction


**Limitations**

Negative samples are synthetic (not actual safe-driving records)

Prototype-level (expand data for production use)


**Contributions**

Got ideas? Found a bug? Open an issue or PR — contributions welcome!


How to Contribute:  

Fork the repo  

Create a branch: git checkout -b your-feature`  

Make your changes


Commit: 

git commit -m "Add: your feature"`  

Push and open a pull request  


**Guidelines**

Write clean, modular Python code  

Use clear commit messages  

Document functions with simple docstrings

Thanks for helping make this project better!

**Let’s make our roads safer — one prediction at a time!**
