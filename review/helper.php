<?php

define("DATASET_FILE", __DIR__ . "/data/dataset_assistant_2313500122.csv");

define("PROGRESS_FILE", __DIR__ . "/data/review_progress.json");

/* ==========================================================
   LOAD DATASET
========================================================== */

function loadDataset()
{
    $rows = [];

    if (!file_exists(DATASET_FILE)) {
        return $rows;
    }

    $fp = fopen(DATASET_FILE, "r");

    // ==========================
    // HEADER
    // ==========================

    $header = fgetcsv($fp);

    if (!$header) {
        fclose($fp);
        return [];
    }

    // Bersihkan BOM dan spasi
    $header = array_map(function ($item) {

        $item = preg_replace('/^\xEF\xBB\xBF/', '', $item);

        return trim($item);

    }, $header);

    // ==========================
    // DATA
    // ==========================

    while (($row = fgetcsv($fp)) !== false) {

        if (count($row) != count($header)) {
            continue;
        }

        $rows[] = array_combine($header, $row);

    }

    fclose($fp);

    return $rows;
}

/* ==========================================================
   LOAD PROGRESS
========================================================== */

function loadProgress()
{

    if (!file_exists(PROGRESS_FILE)) {

        return [

            "last_page" => 1,

            "updated_at" => "",

            "review" => []

        ];

    }

    $json = file_get_contents(PROGRESS_FILE);

    $data = json_decode($json, true);

    if (!$data) {

        return [

            "last_page" => 1,

            "updated_at" => "",

            "review" => []

        ];

    }

    return $data;

}

/* ==========================================================
   SAVE PROGRESS
========================================================== */

function saveProgress($progress)
{

    file_put_contents(

        PROGRESS_FILE,

        json_encode(

            $progress,

            JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE

        )

    );

}

/* ==========================================================
   TOTAL DATA
========================================================== */

function totalData()
{

    return count(

        loadDataset()

    );

}

/* ==========================================================
   PAGINATION
========================================================== */

function getPageData($dataset, $page = 1, $perPage = 20)
{

    $offset = ($page - 1) * $perPage;

    return array_slice(

        $dataset,

        $offset,

        $perPage

    );

}

/* ==========================================================
   TOTAL PAGE
========================================================== */

function totalPage($dataset, $perPage = 20)
{

    return ceil(

        count($dataset) / $perPage

    );

}

/* ==========================================================
   REVIEW COUNT
========================================================== */

function reviewedCount($progress)
{

    return count(

        $progress["review"]

    );

}

/* ==========================================================
   PROGRESS PERCENT
========================================================== */

function progressPercent($dataset, $progress)
{

    if (count($dataset) == 0)

        return 0;

    return round(

        reviewedCount($progress)

        /

        count($dataset)

        *

        100,

        2

    );

}

/* ==========================================================
   BADGE COLOR
========================================================== */

function badgeColor($label)
{

    switch ($label) {

        case "positive":

            return "success";

        case "negative":

            return "danger";

        default:

            return "secondary";

    }

}

function getTweet($row)
{
    $possible = [

        "full_text",

        "text",

        "tweet",

        "content"

    ];

    foreach ($possible as $field) {

        if (
            isset($row[$field]) &&
            trim($row[$field]) != ""
        ) {
            return $row[$field];
        }

    }

    return "(Tweet tidak ditemukan)";
}