import React, { Component } from 'react';
import { LineChart, Line, Tooltip, YAxis, XAxis, ResponsiveContainer } from 'recharts';

function UserView(props) {
    const user = props.user;
    const data = props.data;
    const link = "https://www.instagram.com/" + user.instagram + "/"

    const hasInsta = user.instagram.length > 0;
    const hasFollowerData = user.data_points && user.data_points.length > 0;

    return (
        <div className="user-view">
            <div className="user-info">
                <div className="user-image">
                    <img src={user.image_url}/>
                </div>
                <div className="user-name">
                    <p>
                        {user.name}
                    </p>
                    {hasInsta && 
                        <p className="user-handle">
                            <a href={link}>
                                {"@" + user.instagram}
                            </a>
                        </p>
                    }
                </div>
            </div>
            {hasFollowerData && 
                <div className="follower-count">
                    <span>Followers: </span>
                    <span>{data[data.length - 1].followers}</span>
                </div>
            }
            {hasFollowerData &&
                <div className="chart-view">
                    <ResponsiveContainer width='100%' height={250}>
                        <LineChart 
                            data={data}
                            margin={{ top: 5, right: 5, bottom: 5, left: 5 }}
                        >
                            <Line type="monotone" dataKey="followers" stroke="#8884d8" />
                            <YAxis 
                                type="number" 
                                domain={['dataMin', 'dataMax']} 
                                orientation="right" 
                                // padding={{ top: , bottom: 20, left: 20 }}
                                axisLine={false}
                                tickLine={false}
                                hide={true}
                            />
                            <XAxis 
                                dataKey="name" 
                                padding={{right: 30}}
                                axisLine={false}
                                tickLine={false}
                                hide={true}
                            />
                            <Tooltip />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            }
        </div>
    )
}

export default UserView;