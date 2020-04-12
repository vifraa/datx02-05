import React, { Component } from 'react'

export default class modelCardsContainer extends Component {
    
    constructor(props) {
        super(props);
        this.state = {model_names_and_images:{}}
    }

    componentDidMount() {
        fetch("https://localhost:5000/models")
            .then(res => res.json())
            .then((data) => {
                this.setState({model_names_and_images : data});
            }).catch(console.log);
    }

    render() {
        console.log(this.state);
        return (
            <div>
                modelCardsContainer
            </div>
        )
    }
} 
