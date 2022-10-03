import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const key = 'HolbertonSchools';
const fields = ['Portland', 'Seattle', 'NewYork', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2,]

fields.forEach((field, index) => {
    client.hset(key, field, values[index], redis.print);
});

client.hgetall(key, (err, value) => {
    console.log(value);
});
