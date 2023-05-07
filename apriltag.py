import apriltag
import numpy as np

camera_params = "camera calibration/CameraCalibration.npz"
# Load camera parameters
with np.load(camera_params) as file:
    cameraMatrix, dist, rvecs, tvecs = [
        file[i] for i in ("cameraMatrix", "dist", "rvecs", "tvecs")
    ]
aprilCameraMatrix = [
    cameraMatrix[0][0],
    cameraMatrix[1][1],
    cameraMatrix[0][2],
    cameraMatrix[1][2],
]
options = apriltag.DetectorOptions(
    families="tag16h5",
    nthreads=3,
    quad_decimate=2.0,
    quad_sigma=3.0,
    decode_sharpening=1.0,
    refine_edges=3,
)
detector = apriltag.Detector()


def get_tag(image):
    # get the apriltag closest to the center of the screen and return its x,y coordinates from the center
    results = detector.detect(
        image, estimate_tag_pose=False, camera_params=aprilCameraMatrix, tag_size=0.2032
    )

    if len(results) > 0:
        return int(results[0].center[0]), int(results[0].center[1])
    else:
        return None, None
