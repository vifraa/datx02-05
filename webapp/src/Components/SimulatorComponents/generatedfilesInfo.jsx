import React, { Component } from 'react';
import GeneratedFileCardContainer from './generatedFileCardContainer';

export default class generatedfilesInfo extends Component {
    render() {
        return (
            <div>
                <div className="section_title">
                    <h3>Generated files:</h3>

                    <div id="generated_files" className="information_section">
                        <GeneratedFileCardContainer />
                    </div>
                </div>
            </div>
        )
    }
}
