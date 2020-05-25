import React, { Component } from 'react';
import GeneratedFileCardContainer from './generatedFileCardContainer';

export default class generatedfilesInfo extends Component {
    render() {
        return (
            <div>
                <div>
                    <h5>Generated files:</h5>
                    <div id="generated_files" className="information_section">
                        <GeneratedFileCardContainer />
                    </div>
                </div>
            </div>
        )
    }
}
