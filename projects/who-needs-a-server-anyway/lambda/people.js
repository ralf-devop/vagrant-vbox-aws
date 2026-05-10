exports.handler = async (event) => {
    return {
        statusCode: 200,
        headers: { "Content-Type": "text/plain" },
        body: JSON.stringify([{id: 1, name: "Max"}, {id: 2, name: "Anna"}, {id: 3, name: "Lukas"}, {id: 4, name: "Sophie"}, {id: 5, name: "Leon"}]),
    };
};