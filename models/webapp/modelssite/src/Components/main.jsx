import React, { Component } from 'react';
import ModelsContainer from './modelCardsContainer';
import UploadData from './uploadData.jsx'

class main extends Component {
    render() {
        return (
            <div>
                <UploadData/>
                <ModelsContainer/>
            </div>
        );
    }
}

export default main;