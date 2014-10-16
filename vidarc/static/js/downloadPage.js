require(['./common'], function(common){
    require(['app/download']);
});

function FreshBox(options) {
    this.xhr = XMLHttpRequest();
    this.xhr.open('GET', options.url, true);
    this.xhr.onreadystatechange = this.onReadyStateChange.bind(this);
    this.send()
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

