import React, { Component } from 'react'

class ttrrecengine extends React.Component {

    constructor(props){
        super(props)
    }

    componentDidMount(){
        window.location = "http://127.0.0.1:5000/ttr"
    }

    render(){
        return null
    }

}

export default ttrrecengine