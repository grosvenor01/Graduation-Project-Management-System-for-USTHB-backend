
import React from 'react';
function Progress({percent='0%'}) {
    return(
        <div className="outer-prg">
            <div className="inner-prg" style={{'--width':percent}}>progress</div>
        </div>
    )
}

export default Progress