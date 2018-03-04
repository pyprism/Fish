const path = require("path");
module.exports = {
    entry: ["./static/components/notebooks.js"],
    output: {
        path: path.resolve(__dirname, "static"),
        filename: "js/[name].js"
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
            ]
    }
};