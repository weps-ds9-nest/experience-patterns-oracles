# By ChatGPT, Dalle 3

By ChatGPT, Dalle 3

I hate trying to import files using the importer… It is so hard to find the one that I am looking for!

So!

In this article, I would like to share with you really quick on how we can add Drag and Drop support for file upload!

The idea is simple!

Use the [**HTML Drag and Drop API**](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)!

However, there are just so many other information that we don’t need (for this capability) in the official document so I decided to pull up this little article to share with you a simple code snippet for file drag and drop to get you started on fly!

## Code

Yes, let’s start with the code.

I have also created a little [**_codepen_**](https://codepen.io/0ITSUKI0/pen/GRVzxgb) for this so you can also give it a try there!

### HTML

```
<div id="fileImport">
  File Import Area
</div>

<div id="result"></div>
```

### CSS

```
#fileImport {
  background: #b3b3b3;
  width: 200px;
  height: 120px;
}
```

### Javascript

Script is the key.

```
window.onload = (event) => {
    console.log("page is fully loaded");
    const containerDiv = document.getElementById("fileImport");

    containerDiv.addEventListener("dragover", (e) => {
        e.preventDefault();
        e.dataTransfer.clearData();
        e.dataTransfer.dropEffect = "copy";
    });

    containerDiv.addEventListener("drop", (e) => {
        e.preventDefault();
        const items = Array.from(e.dataTransfer.items);
        if (items.length === 0) {
            return;
        }

        let resultString = "";
        items.forEach((item, i) => {
            if (item.kind === "file") {
                const file = item.getAsFile();
                resultString = `${resultString}<br>${i}: ${file.name}`;
                document.getElementById("result").innerHTML = resultString;
            }
        });
    });
};
```

There are many other event listeners in the [**Drag and Drop API**](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)**,** but `drop` and `dragover` are the only ones matter here!

## Get Itsuki’s stories in your inbox

Join Medium for free to get updates from this writer.

We don’t need `dragStart`, don’t need `event.dataTransfer.setData`, none of those!

`dragover` event handler is here mainly to turn off the browser's default drag behavior, which is not allowing any drag and drop.

And `drop` is where we will retrieve the dropped file contents. I am simply displaying the file names here in the `result` div, but (obviously), you will be doing something more interesting here, for example, posting the file to the server.

I have added the event listeners using Javascript, but you can also use `ondrop` for the `drop` event listener and `ondragover` for `dragover` like following.

`<div id="fileImport" ondrop="drop(event)" ondragover="allowDrop(event)"></div>`
## Demo

That’s it for the code!

Let’s check it out to see how we are doing!

Yeah!

## Related
[Add wiki-links manually or run update_wikilinks.py]