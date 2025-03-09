function findStronglyRecommendedTracks(t, testCases) {
    let results = [];
    
    for (let caseIndex = 0; caseIndex < t; caseIndex++) {
        let [n, segments] = testCases[caseIndex];
        let recommendedCounts = new Array(n).fill(0);
        let usersSegments = segments.map(([l, r]) => [l, r]);

        for (let i = 0; i < n; i++) {
            let [li, ri] = usersSegments[i];
            let predictors = [];

            for (let j = 0; j < n; j++) {
                if (i !== j) {
                    let [lj, rj] = usersSegments[j];
                    if (lj <= li && ri <= rj) {
                        predictors.push([lj, rj]);
                    }
                }
            }

            if (predictors.length === 0) {
                recommendedCounts[i] = 0;
                continue;
            }

            let intersectionL = Math.max(...predictors.map(([lj]) => lj));
            let intersectionR = Math.min(...predictors.map(([_, rj]) => rj));
            
            if (intersectionL <= intersectionR) {
                let totalRecommended = (intersectionR - intersectionL + 1) - Math.max(0, ri - li + 1);
                recommendedCounts[i] = totalRecommended;
            } else {
                recommendedCounts[i] = 0;
            }
        }

        results.push(recommendedCounts);
    }

    return results;
}

function main() {
    const t = parseInt(prompt("Enter number of test cases: "), 10);
    let testCases = [];

    for (let i = 0; i < t; i++) {
        const n = parseInt(prompt("Enter number of segments: "), 10);
        let segments = [];
        
        for (let j = 0; j < n; j++) {
            const input = prompt("Enter segment (l r): ").split(" ").map(Number);
            segments.push([input[0], input[1]]);
        }
        
        testCases.push([n, segments]);
    }

    let results = findStronglyRecommendedTracks(t, testCases);
    
    results.forEach(result => console.log(result.join("\n")));
}

main();