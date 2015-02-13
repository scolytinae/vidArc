define(['app/longPolling'], function(LongPolling) {
    function FreshBox(options) {
        console.log('start init');
        this.downloadItems = [];
        this.url = options.url;
        this.itemTemplate = options.itemTemplate;

        this.widget = options.downloadWidget;
        this.downloadList = this.widget.querySelector("#download-list");
        this.downloadForm = this.widget.querySelector("#download-form");
        this.downloadInput = this.widget.querySelector("#address");
        this.errorsDiv = this.downloadForm.querySelector(".download-errors");

        this.downloadForm.onsubmit = this.onSubmit.bind(this);

        this.lp = new LongPolling(this.url);
        this.lp.on("addItem", this.onAddItem.bind(this));
        this.lp.on("delItem", this.onDelItem.bind(this));
        this.lp.start();

        console.log('start polling');
    }

    FreshBox.prototype.onSubmit = function(e) {
        var xhr = new XMLHttpRequest();
        console.log('post' + this.downloadInput.text);
        xhr.open("POST", this.url, true);
        xhr.send("url=" + this.downloadInput.text);
        this.downloadForm.text = "";
        return false;
    }

    FreshBox.prototype.onAddItem = function(e) {
        var div = this.downloadItems[e.id];
        if (!div) {
            div = document.createElement("div");
            this.downloadList.appendChild(div);
        }
        div.innerHTML = this.itemTemplate({'type': e.id, 'title': e.title});

        this.downloadItems[e.id] = div;
    };


    FreshBox.prototype.onDelItem = function(e) {

    };

    return FreshBox;
});