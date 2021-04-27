import React, { Component } from 'react';
import { Chart } from "react-google-charts"; 
class PressureChart extends Component {
   
    render() {
        //get data from json
        let theData = this.props.data
        //for google chart format
        let d = theData.map(v => ([v.ms ,v.pressure]) );
        // eslint-disable-next-line
        //google charts require header
        d.unshift(["kPa","ms"])
      return <div> 
          <center><b>Pressure Analytics</b></center>      
          <Chart
      chartType="LineChart"
      data={d}
      width="100%"
      height="400px"
    /></div>;
    }
  }
  export default PressureChart;