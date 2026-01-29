import json
import os
import sys

try:
    print("Starting update...")
    notebook_path = r"c:\Users\lamph\github\DataScience\scikit-learn\Plus_6_LinearRegressionModel.ipynb"
    
    if not os.path.exists(notebook_path):
        print(f"Error: {notebook_path} not found")
        sys.exit(1)

    print("Reading file...")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    print("File read.")

    new_cell = {
       "cell_type": "code",
       "execution_count": None,
       "id": "visualize_map",
       "metadata": {},
       "outputs": [],
       "source": [
        "import matplotlib.pyplot as plt\n",
        "import urllib.request\n",
        "import os\n",
        "\n",
        "# 캘리포니아 지도 다운로드\n",
        "images_path = \"images\"\n",
        "os.makedirs(images_path, exist_ok=True)\n",
        "filename = \"california.png\"\n",
        "filepath = os.path.join(images_path, filename)\n",
        "\n",
        "if not os.path.isfile(filepath):\n",
        "    url = \"https://github.com/ageron/handson-ml3/raw/main/images/end_to_end_project/\" + filename\n",
        "    urllib.request.urlretrieve(url, filepath)\n",
        "\n",
        "california_img = plt.imread(filepath)\n",
        "\n",
        "ax = df.plot(kind=\"scatter\", x=\"Longitude\", y=\"Latitude\", figsize=(10,7),\n",
        "             s=df[\"Population\"]/100, label=\"Population\",\n",
        "             c=\"medHouseVa\", cmap=\"jet\", colorbar=True,\n",
        "             alpha=0.4, sharex=False)\n",
        "\n",
        "plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5,\n",
        "           cmap=plt.get_cmap(\"jet\"))\n",
        "plt.ylabel(\"Latitude\", fontsize=14)\n",
        "plt.xlabel(\"Longitude\", fontsize=14)\n",
        "\n",
        "plt.legend(fontsize=16)\n",
        "plt.show()"
       ]
    }

    # Check if cell already exists to avoid duplication
    ids = [c.get('id', '') for c in nb['cells']]
    if "visualize_map" in ids:
        print("Cell already exists. Skipping.")
    else:
        nb['cells'].append(new_cell)
        print("Cell appended.")

        print("Writing file...")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print("File written.")

except Exception as e:
    print(f"Error: {e}")
