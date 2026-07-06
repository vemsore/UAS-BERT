<?php

require_once "helper.php";

/* ==========================================================
LOAD DATA
========================================================== */

$dataset = loadDataset();

$progress = loadProgress();

$gold = [];

foreach ($dataset as $index => $row) {

    // -------------------------------
    // Gunakan label hasil review jika ada
    // -------------------------------

    if (isset($progress["review"][$index])) {

        $label = $progress["review"][$index]["label"];

    } else {

        // jika belum direview
        // gunakan suggestion AI

        $label = $row["suggestion"];

    }

    // -------------------------------
    // Dataset Gold
    // -------------------------------

    $gold[] = [

        "full_text"        => $row["full_text"],

        "label"            => $label,

        "suggestion"       => $row["suggestion"],

        "confidence"       => $row["confidence"],

        "need_review"      => $row["need_review"],

        "positive_score"   => $row["positive_score"],

        "negative_score"   => $row["negative_score"],

        "policy_score"     => $row["policy_score"]

    ];

}

/* ==========================================================
SAVE
========================================================== */

$file = __DIR__ .
"/data/dataset_gold_2313500122.csv";

$fp = fopen($file,"w");

fputcsv(

    $fp,

    array_keys($gold[0])

);

foreach($gold as $row){

    fputcsv(

        $fp,

        $row

    );

}

fclose($fp);

/* ==========================================================
DOWNLOAD
========================================================== */

header("Content-Type:text/csv");

header(

'Content-Disposition: attachment; filename="dataset_gold_2313500122.csv"'

);

readfile($file);

exit;