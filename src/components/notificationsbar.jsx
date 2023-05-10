import { faXmark } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { useState } from 'react';
import Notif from './notif';
import React from 'react';
function NotificationsBar({open, onClose}){

    if(!open) return null
    return (
        (
            <div className="notifpopup">
            <div className="notifbar">
            <div className='mark'>
                <h1>Notification</h1>
                <FontAwesomeIcon icon={faXmark} className='faxmark' onClick={onClose}/> 
            </div>
            <h3>Voir tout</h3>
            <Notif/>
            <Notif/>
           </div>
        </div>
        )
    ) 
}

export default NotificationsBar