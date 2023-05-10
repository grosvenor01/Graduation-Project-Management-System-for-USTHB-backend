import React from 'react';
function Circularprogress({persentage,circleWidth}) {

    const radius = 85;
    const dashArray = radius * Math.PI * 2;
    const dashOffset = dashArray - (dashArray * persentage) / 100

    return(
        <div>
            <svg 
            width={circleWidth}
            height={circleWidth}
            viewBox={`0 0 ${circleWidth} ${circleWidth}`}
            >
                <circle
                cx={circleWidth / 2}
                cy={circleWidth / 2}
                strokeWidth="15px"
                r="80"
                className="circle-background"
                />

               <circle
                cx={circleWidth / 2}
                cy={circleWidth / 2}
                strokeWidth="15px"
                r="80"
                className="circle-progress"
                style={{
                    strokeDasharray : dashArray,
                    strokeDashoffset : dashOffset
                }}
                transform={`rotate(-90 ${circleWidth / 2} ${circleWidth / 2})`}
                />
                <text 
                x="50%" 
                y="50%" 
                dy="0.3em" 
                textAnchor="middle" 
                className="circle-text" >
                    {persentage} %
                </text>
            </svg>
        </div>
    )
}

export default Circularprogress