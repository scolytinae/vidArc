define(function() {
    function FreshBox(options) {
        console.log(options.elem);
        console.log(options.url);
        this.xhr = XMLHttpRequest();
        this.xhr.open('GET', options.url, true);
        this.xhr.onreadystatechange = this.onReadyStateChange.bind(this);
        this.xhr.send();
    }

    FreshBox.prototype.addDownloadInfo = function(info) {

    }

    FreshBox.prototype.delDownloadInfo = function(info) {

    }

    FreshBox.prototype.onReadyStateChange = function() {
        if (this.xhr.readyState != 4) return;

        if (this.xhr.status != 200) {
            console.log(this.xhr.status + ': ' + this.xhr.statusText);
        } else {
            console.log(this.xhr.responseText);
        }
    //this.xhr.send();
    }

    return FreshBox;
});