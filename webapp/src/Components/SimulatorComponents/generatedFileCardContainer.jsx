import React, { Component } from 'react'
import GeneratedFileCard from './generatedFileCard';
import Button from 'react-bootstrap/Button';

export default class generatedFileCardContainer extends Component {

    constructor(props) {
        super(props);
        this.state = {
            gen_files: []
        };
    }

    
    checkgenerated() {
        fetch("http://127.0.0.1:5000/simulator/generatedfiles")
            .then(res => res.json())
            .then((data) => {
                this.setState({ gen_files: data });
            }).catch(console.log);
    }
    

    render() {
        console.log(this.state)
        return (
            <div>
                <div className="d-flex bd-highlight example-parent ">
                    {this.state.gen_files.map((gen_file, idx) => {
                        return <GeneratedFileCard
                            csvName={gen_file[0]}
                            csvShape={gen_file[1][0] + 'x' + gen_file[1][1]}
                            key={idx}
                        />
                    })}
                </div>
                <Button style={{width: '15%', marginTop: '10px'}} onClick={()=>{this.checkgenerated()}}>Refresh after generating data</Button>
            </div>
        )
    }
}
