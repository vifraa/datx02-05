import React from 'react';
import { TriangleSkewSpin	 } from 'react-pure-loaders';

class AwesomeComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true
    }
  }
  render() {
    return (
      <div>
        <TriangleSkewSpin	
          color={'#ffffff'}
          loading={this.props.loading}
        />
      </div>
    )
  }
}
export default AwesomeComponent;
