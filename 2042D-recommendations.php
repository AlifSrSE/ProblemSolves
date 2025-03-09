<?php

function find_strongly_recommended_tracks($t, $test_cases) {
    $results = [];

    foreach ($test_cases as $case) {
        list($n, $segments) = $case;
        $recommended_counts = array_fill(0, $n, 0);
        $users_segments = $segments;

        for ($i = 0; $i < $n; $i++) {
            list($li, $ri) = $users_segments[$i];
            $predictors = [];

            for ($j = 0; $j < $n; $j++) {
                if ($i != $j) {
                    list($lj, $rj) = $users_segments[$j];
                    if ($lj <= $li && $ri <= $rj) {
                        $predictors[] = [$lj, $rj];
                    }
                }
            }

            if (empty($predictors)) {
                $recommended_counts[$i] = 0;
                continue;
            }

            $intersection_l = max(array_column($predictors, 0));
            $intersection_r = min(array_column($predictors, 1));
            if ($intersection_l <= $intersection_r) {
                $total_recommended = ($intersection_r - $intersection_l + 1) - max(0, $ri - $li + 1);
                $recommended_counts[$i] = $total_recommended;
            } else {
                $recommended_counts[$i] = 0;
            }
        }

        $results[] = $recommended_counts;
    }

    return $results;
}

function main() {
    $t = intval(trim(fgets(STDIN)));
    $test_cases = [];

    for ($i = 0; $i < $t; $i++) {
        $n = intval(trim(fgets(STDIN)));
        $segments = [];
        for ($j = 0; $j < $n; $j++) {
            $segments[] = array_map('intval', explode(' ', trim(fgets(STDIN))));
        }
        $test_cases[] = [$n, $segments];
    }

    $results = find_strongly_recommended_tracks($t, $test_cases);

    foreach ($results as $result) {
        echo implode("\n", $result) . "\n";
    }
}

main();
?>