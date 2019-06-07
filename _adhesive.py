from gbs_pipeline import pipeline_build_gbs_images


pipeline_build_gbs_images({
    "base_containers": {
        "ubuntu-18.04": "germaniumhq/ubuntu:18.04",
    }
})

