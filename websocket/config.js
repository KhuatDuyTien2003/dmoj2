// module.exports = {
//     get_host: '192.168.1.6',
//     get_port: 15100,
//     post_host: '192.168.1.6',
//     post_port: 15101,
//     http_host: '192.168.1.6',
//     http_port: 15102,
//     long_poll_timeout: 29000,
// };

module.exports = {
    get_host: process.env.GET_HOST || 'default_get_host',
    get_port: process.env.GET_PORT || 15100,
    post_host: process.env.POST_HOST || 'default_post_host',
    post_port: process.env.POST_PORT || 15101,
    http_host: process.env.HTTP_HOST || 'default_http_host',
    http_port: process.env.HTTP_PORT || 15102,
    long_poll_timeout: process.env.LONG_POLL_TIMEOUT || 29000, 
};
