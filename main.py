from flask import Flask, request, jsonify, render_template
import openai

openai.api_key = "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"
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("front.html" , )


img_sizes = {"small": "256x256", "medium": "512x512", "large": "1024x1024"}


@app.route("/generate", methods=["GET"])
def ai():
    image_text = request.args.get("image")
    image_size = request.args.get("size")
    img_count = request.args.get("count")
    print(image_text, image_size, img_count)
    response = openai.Image.create(
        prompt=image_text,
        n=int(img_count) if img_count is not None else 1,
        size=img_sizes[image_size],
    )
    print(response["data"])
    image_urls = {
        index: image_url["url"] for index, image_url in enumerate(response["data"])
    }
    res = jsonify({"image_url": image_urls})
    print(res.data)
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res


if __name__ == "__main__":
    app.run(debug=False ,host= '0.0.0.0')
