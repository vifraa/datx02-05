import React, { Component } from 'react'
import modelCard from './modelCard';

export default class modelCardsContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            model_names_and_images:{}
        }
    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/models")
            .then(res => res.json())
            .then((data) => {
                this.setState({model_names_and_images : data});
            }).catch(console.log);
    }

    render() {
        console.log(this.state);
        return (
            <div>
                {this.state.model_names_and_images.map((model, idx) => {
                    return <modelCard
                            model_name={model.model_name} 
                            model_img={model.model_img}
                            key={idx} 
                        /> 
                })}
                            
                <pre id="regression_output">Here you will see the results of th regression..</pre>
            </div>
        )
    }
} 
