import data1 from "../Data/data1"
import Box from "./box"
import React from 'react';
function Numbers (){

    const boxs= data1.map(item => {
        return (
          <Box 
            key={item.id}
            {...item}
          />
        )
      })

    return(
        <div className="numbers">
            {boxs}
        </div>
    )
}

export default Numbers