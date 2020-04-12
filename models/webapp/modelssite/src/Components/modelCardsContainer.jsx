import React, { Component } from 'react'

export default class modelCardsContainer extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            model_names_and_images:{},
            regression_results:""
        }
    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/models")
            .then(res => res.json())
            .then((data) => {
                this.setState({model_names_and_images : data});
            }).catch(console.log);
    }

    run_regression(ModelName){
        fetch("http://127.0.0.1:5000/models/regression/" + ModelName)
        .then(res => res.json())
        .then((data) => {
            this.setState({regression_results : data});
            this.write_text("regression_output", data);
        }).catch(console.log);
    }

    write_text(element_id, txt){
        document.getElementById(element_id).text(txt);
    }

    render() {
        console.log(this.state);
        return (
            <div>
                <button type="button" className="btn btn-primary mr-2" onClick={()=>{this.run_regression('Lasso')}}>Lasso</button>
                <button type="button" className="btn btn-primary mr-2" onClick={()=>{this.run_regression('Ridge')}}>Ridge</button>
                <button type="button" className="btn btn-primary mr-2" onClick={()=>{this.run_regression('ElasticNet')}}>Elastic Net</button>
                <button type="button" className="btn btn-primary mr-2" onClick={()=>{this.run_regression('DecisionTree')}}>Decision Tree</button>
                <button type="button" className="btn btn-primary mr-2" onClick={()=>{this.run_regression('RandomForest')}}>Random Forest</button>
                <button type="button" className="btn btn-primary mr-2" onClick={()=>{this.run_regression('NeuralNetwork')}}>Neural Network</button>
                <pre id="regression_output">Here you will see the results of th regression..</pre>
            </div>
        )
    }
} 
