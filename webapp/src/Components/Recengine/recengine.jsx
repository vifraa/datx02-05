import React, { Component } from 'react'

class recengine extends React.Component {

    constructor(props){
        super(props)
    }

    componentDidMount(){
        window.location = "http://127.0.0.1:5000/"
    }

    render(){
        return null
    }

}

export default recengine