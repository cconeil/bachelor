import React, { Component } from 'react';
import { LineChart, Line, Tooltip, YAxis, XAxis, ResponsiveContainer } from 'recharts';

function UserView(props) {
    const user = props.user;
    const dataPoints = user.data_points;

    const hasInsta = user.insta && user.insta.length > 0;
    const hasFollowerData = dataPoints && dataPoints.length > 0;

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
                            <a href={"https://www.instagram.com/" + user.insta + "/"}>
                                {"@" + user.insta}
                            </a>
                        </p>
                    }
                </div>
            </div>
            {hasFollowerData && 
                <div className="follower-count">
                    <span>Followers: </span>
                    <span>{dataPoints[dataPoints.length - 1].num_followers}</span>
                </div>
            }
            {user.delta &&
                <div className="follower-delta">
                    {user.delta > 0 &&
                        <div className="up">
                            <span>Up</span>
                            <span>{user.delta}</span>
                        </div>
                    }
                    {user.delta < 0 &&
                        <div className="down">
                            <span>Down</span>
                            <span>{user.delta}</span>
                        </div>
                    }
                </div>
            }
            {hasFollowerData &&
                <div className="chart-view">
                    <ResponsiveContainer width='100%' height={250}>
                        <LineChart 
                            data={dataPoints}
                            margin={{ top: 5, right: 5, bottom: 5, left: 5 }}
                        >
                            <Line type="monotone" dataKey="num_followers" stroke="#8884d8" />
                            <YAxis 
                                type="number" 
                                domain={['dataMin', 'dataMax']} 
                                orientation="right" 
                                axisLine={false}
                                tickLine={false}
                                hide={true}
                            />
                            <XAxis 
                                dataKey="timestamp" 
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