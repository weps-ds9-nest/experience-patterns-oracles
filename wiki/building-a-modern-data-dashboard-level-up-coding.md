# Building A Modern Data Dashboard Level Up Coding

## With source data from a CSV file

## Using Python and the Gradio library

This is the second in a short series on developing data dashboards using the latest Python-based GUI development tools, Streamlit, Gradio and Taipy.

The source data set for each dashboard will be the same but stored in different formats. As much as possible, I’ll also try to make the actual dashboard layouts for each tool resemble each other and have the same functionality.

In the first part of this series, I created a Streamlit version of the dashboard that retrieves its data from a local Postgresql database. A link to that article is at the end of this one.

The data for this dashboard will be in a local CSV file, and Pandas will be our primary data processing engine.

> If you want to see a quick demo of the app, I have deployed it to Hugging Face Spaces. You can run it using the link below, but note that the two input date picker pop-ups do not work due to a known bug in the Hugging Face environment. This is only the case for deployed apps on HF, and you can still change the dates manually. Running the app locally works fine and doesn’t have this issue

[**https://huggingface.co/spaces/taupirho/data-dashboard**](https://huggingface.co/spaces/taupirho/data-dashboard)

### What is Gradio?

Gradio is an open-source Python package that eases the process of building demos or web applications for machine learning models, APIs, or any Python function. With Gradio, you can create stunning demos or web applications without needing JavaScript, CSS, or web hosting experience. By writing just a few lines of Python code, you can unlock the power of Gradio and seamlessly showcase your machine-learning models to a broader audience.

Gradio simplifies the development process by providing an intuitive framework that eliminates the complexities associated with building user interfaces from scratch. Whether you are a machine learning developer, researcher, or enthusiast, Gradio allows you to create beautiful and interactive demos that enhance the understanding and accessibility of your machine learning models.

## Related
[Add wiki-links manually or run update_wikilinks.py]