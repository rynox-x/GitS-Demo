const express = require("express");
const app = express();

app.get("/", (req, res) => {
    const name = req.query.name;

    // XSS
    document.body.innerHTML = name;

    // Dangerous eval
    eval(name);

    res.send(name);
});

app.listen(3000);
