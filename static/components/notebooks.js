import React from "react";
import ReactDOM from "react-dom";
class Notebooks extends React.Component {

    constructor(props){
        super(props);
        this.loadData();
    }

    loadData() {
        $.ajax("/notebook/", {
            contentType: "application/json",
            success: function(data) {
                console.log(data);
            },
            error: function(data) {
                console.error(data);
            }
        });
    }

    render() {
        return (
            <div className="row clearfix">
                <div className="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div className="card">
                        <div className="header">
                            <h2>
                                Basic Card Title
                            </h2>
                        </div>
                        <div className="body">
                            Quis pharetra a pharetra fames blandit. Risus faucibus velit Risus imperdiet mattis neque volutpat, etiam lacinia netus dictum magnis per facilisi sociosqu. Volutpat. Ridiculus nostra.
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
ReactDOM.render(<Notebooks />, document.getElementById("notebooks"));